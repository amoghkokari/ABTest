from helper_func import display_email_campaigns, display_user_personas, display_user_responses, save_as_docx
from agents.email_gen_agent.agent import generate_email_campaigns_for_experiment
from product_input import health_product_description as product_description
from agents.response_sim_agent.agent_workflow import response_to_email
from agents.response_evaluator_agent.agent import evaluate_experiment
from agents.persona_gen_agent.agent import generate_personas
from agents.exp_gen_agent.agent import generate_experiments
from prefect import task, flow, get_run_logger
from argparse import ArgumentParser
from dotenv import load_dotenv
import wandb
import time
import os

load_dotenv()

@task(name="Generate Experiments")
def run_experiment_agent(num_experiments: int, product_description: str):
    logger = get_run_logger()
    start_time = time.time()
    experiments = generate_experiments(num_experiments, product_description)
    duration = round(time.time() - start_time, 2)

    wandb.log({"experiment_id": experiments.experiment_id, "execution_time": duration})

    logger.info(f"✅ Experiment Agent completed in {duration}s. Generated {experiments.experiment_id} experiment.")
    return experiments

@task(name="Generate Email Campaigns")
def run_email_campaign_agent(experiments):
    logger = get_run_logger()

    email_campaign_a, email_campaign_b  = generate_email_campaigns_for_experiment(experiments)

    Campaign_A = {
        "variant":email_campaign_a.variant,
        "subject":email_campaign_a.subject,
        "body":email_campaign_a.body,
        "tone":email_campaign_a.tone,
        "target_audience":email_campaign_a.target_audience
    }
    Campaign_B = {
        "variant":email_campaign_b.variant,
        "subject":email_campaign_b.subject,
        "body":email_campaign_b.body,
        "tone":email_campaign_b.tone,
        "target_audience":email_campaign_b.target_audience
    }

    wandb.log({"email_campaign_a": Campaign_A, "email_campaign_b": Campaign_B})

    logger.info("✅ Email Campaign Agent completed.")
    logger.info(f"Generated campaigns for campaign a : {Campaign_A}")
    logger.info(f"Generated campaigns for campaign a : {Campaign_B}")

    df_email = display_email_campaigns(email_campaign_a, email_campaign_b)
    df_email.to_csv("df_email.csv")
    logger.info(f"Campaign email df saved")

    return email_campaign_a, email_campaign_b 

@task(name="Generate Personas")
def run_persona_agent(email_campaign_a, email_campaign_b, n_participants):
    logger = get_run_logger()
    personas = generate_personas(email_campaign_a, email_campaign_b, n_participants)

    wandb.log({"personas_generated": len(personas.personas)})

    logger.info(f"✅ Persona Agent completed. Generated {len(personas.personas)} personas.")
    for user in personas.personas:
        user_personas = {
            "persona_id":user.persona_id,
            "name":user.name,
            "age":user.age,
            "gender":user.gender,
            "occupation":user.occupation,
            "interests":user.interests,
            "digital_behavior":user.digital_behavior,
            "campaign_varient":user.campaign_varient
        }
        logger.info(f" Persona {user.persona_id} created. Full Persona: {user_personas }")

    df_personas = display_user_personas(personas)
    df_personas.to_csv("df_personas.csv")
    logger.info(f"personas df saved")

    return personas

@task(name="Generate Report")
def run_report_agent(product_input, resp_content, gen_email_campaign_a, gen_email_campaign_b, users_personas, all_user_responses):
    logger = get_run_logger()
    start_time = time.time()

    experiment_valuation = evaluate_experiment(product_input, resp_content, gen_email_campaign_a, gen_email_campaign_b, users_personas, all_user_responses)

    save_as_docx(experiment_valuation, "AB_Test_Report.docx", isWF=True)

    duration = round(time.time() - start_time, 2)

    wandb.log({"experiment_Valuation execution_time": duration})

    logger.info(f"✅ Experiment Agent completed in {duration}s. Generated experiment Report.")
    return experiment_valuation

@flow(name="Simulate Responses")
def run_response_simulation_agent(personas, select_campaign):
    logger = get_run_logger()
    responses, agents = response_to_email(personas, select_campaign)

    wandb.log({"responses_collected": len(responses)})

    logger.info(f"✅ Response Simulation Agent completed. Generated {len(responses)} responses.")

    df_responses = display_user_responses(responses)
    df_responses.to_csv("df_responses.csv")
    logger.info(f"responses df saved")

    return responses

@flow(name="Agentic Experiment Workflow")
def agentic_experiment_pipeline(product_description: str, num_experiments: int = 1, total_personas: int = 5):
    logger = get_run_logger()
    logger.info("🚀 Starting Agentic Experiment Workflow...")

    experiments = run_experiment_agent(num_experiments, product_description)
    email_campaign_a, email_campaign_b = run_email_campaign_agent(experiments)
    personas = run_persona_agent(email_campaign_a, email_campaign_b, total_personas)

    select_campaign = {'A':email_campaign_a, 'B':email_campaign_b}

    user_response = run_response_simulation_agent(personas, select_campaign)

    run_report_agent(product_description, experiments, email_campaign_a, email_campaign_b, personas, user_response)

    logger.info("✅ Experiment Workflow Completed Successfully, Reports and file present in execution directory!")

if __name__ == "__main__":
    wandb.login(key=os.environ.get('WANDB_API'))
    wandb.init(project="agentic_experiment", job_type="experiment_tracking")

    parser = ArgumentParser(description="Run workflow with optional number of personas.")
    parser.add_argument('--personas', type=int, default=5, help='Number of personas to use (default: 5)')

    args = parser.parse_args()

    agentic_experiment_pipeline(product_description(), num_experiments=1, total_personas=args.personas)
    wandb.finish()