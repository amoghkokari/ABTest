from helper_func import display_email_campaigns, display_user_personas, display_user_responses, save_as_docx
from agents.Email_Generator.agent import generate_email_campaigns_for_experiment
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

# Load environment variables from .env file
load_dotenv()

@task(name="Generate Experiments")
def run_experiment_agent(num_experiments: int, product_description: str):
    """
    Task to generate experiment designs for A/B testing.
    
    Args:
        num_experiments (int): Number of experiments to generate
        product_description (str): Description of the product being tested
        
    Returns:
        experiments: Object containing experiment details
    """
    # Get logger from Prefect
    logger = get_run_logger()
    
    # Track execution time
    start_time = time.time()
    
    # Call the agent to generate experiments
    experiments = generate_experiments(num_experiments, product_description)
    
    # Calculate duration
    duration = round(time.time() - start_time, 2)

    # Log metrics to Weights & Biases
    wandb.log({"experiment_id": experiments.experiment_id, "execution_time": duration})

    # Log completion to Prefect
    logger.info(f"✅ Experiment Agent completed in {duration}s. Generated {experiments.experiment_id} experiment.")
    
    return experiments

@task(name="Generate Email Campaigns")
def run_email_campaign_agent(experiments):
    """
    Task to generate email campaigns A and B based on experiment design.
    
    Args:
        experiments: Experiment design object from previous task
        
    Returns:
        tuple: (email_campaign_a, email_campaign_b) containing both email campaign objects
    """
    # Get logger from Prefect
    logger = get_run_logger()

    # Generate two email campaigns (A and B) based on experiment design
    email_campaign_a, email_campaign_b = generate_email_campaigns_for_experiment(experiments)

    # Create dictionary for Campaign A for logging
    Campaign_A = {
        "variant": email_campaign_a.variant,
        "subject": email_campaign_a.subject,
        "body": email_campaign_a.body,
        "tone": email_campaign_a.tone,
        "target_audience": email_campaign_a.target_audience
    }
    
    # Create dictionary for Campaign B for logging
    Campaign_B = {
        "variant": email_campaign_b.variant,
        "subject": email_campaign_b.subject,
        "body": email_campaign_b.body,
        "tone": email_campaign_b.tone,
        "target_audience": email_campaign_b.target_audience
    }

    # Log campaign details to Weights & Biases
    wandb.log({"email_campaign_a": Campaign_A, "email_campaign_b": Campaign_B})

    # Log completion and campaign details to Prefect
    logger.info("✅ Email Campaign Agent completed.")
    logger.info(f"Generated campaigns for campaign a : {Campaign_A}")
    logger.info(f"Generated campaigns for campaign b : {Campaign_B}")  # Fixed typo from "a" to "b"

    # Convert email campaigns to DataFrame and save to CSV
    df_email = display_email_campaigns(email_campaign_a, email_campaign_b)
    df_email.to_csv("df_email.csv")
    logger.info(f"Campaign email df saved")

    return email_campaign_a, email_campaign_b 

@task(name="Generate Personas")
def run_persona_agent(email_campaign_a, email_campaign_b, n_participants):
    """
    Task to generate user personas for A/B testing.
    
    Args:
        email_campaign_a: Email campaign A object
        email_campaign_b: Email campaign B object
        n_participants (int): Number of user personas to generate
        
    Returns:
        personas: Object containing all generated user personas
    """
    # Get logger from Prefect
    logger = get_run_logger()
    
    # Generate personas based on target audiences of both campaigns
    personas = generate_personas(email_campaign_a, email_campaign_b, n_participants)

    # Log metrics to Weights & Biases
    wandb.log({"personas_generated": len(personas.personas)})

    # Log completion to Prefect
    logger.info(f"✅ Persona Agent completed. Generated {len(personas.personas)} personas.")
    
    # Log details of each persona
    for user in personas.personas:
        user_personas = {
            "persona_id": user.persona_id,
            "name": user.name,
            "age": user.age,
            "gender": user.gender,
            "occupation": user.occupation,
            "interests": user.interests,
            "digital_behavior": user.digital_behavior,
            "campaign_varient": user.campaign_varient
        }
        logger.info(f" Persona {user.persona_id} created. Full Persona: {user_personas}")

    # Convert personas to DataFrame and save to CSV
    df_personas = display_user_personas(personas)
    df_personas.to_csv("df_personas.csv")
    logger.info(f"personas df saved")

    return personas

@task(name="Generate Report")
def run_report_agent(product_input, resp_content, gen_email_campaign_a, gen_email_campaign_b, users_personas, all_user_responses):
    """
    Task to generate the final experiment report based on all collected data.
    
    Args:
        product_input (str): Product description
        resp_content: Experiment design object
        gen_email_campaign_a: Email campaign A object
        gen_email_campaign_b: Email campaign B object
        users_personas: User personas object
        all_user_responses: List of user responses
        
    Returns:
        experiment_valuation: Object containing the final experiment report
    """
    # Get logger from Prefect
    logger = get_run_logger()
    
    # Track execution time
    start_time = time.time()

    # Generate experiment valuation report
    experiment_valuation = evaluate_experiment(
        product_input, 
        resp_content, 
        gen_email_campaign_a, 
        gen_email_campaign_b, 
        users_personas, 
        all_user_responses
    )

    # Save report as DOCX file
    save_as_docx(experiment_valuation, "AB_Test_Report.docx", isWF=True)

    # Calculate duration
    duration = round(time.time() - start_time, 2)

    # Log metrics to Weights & Biases
    wandb.log({"experiment_Valuation execution_time": duration})

    # Log completion to Prefect
    logger.info(f"✅ Experiment Agent completed in {duration}s. Generated experiment Report.")
    
    return experiment_valuation

@flow(name="Simulate Responses")
def run_response_simulation_agent(personas, select_campaign):
    """
    Flow to simulate user responses to email campaigns.
    
    Args:
        personas: User personas object
        select_campaign: Dictionary containing both email campaigns
        
    Returns:
        responses: List of user responses to the campaigns
    """
    # Get logger from Prefect
    logger = get_run_logger()
    
    # Simulate user responses to email campaigns
    responses, _ = response_to_email(personas, select_campaign)

    # Log metrics to Weights & Biases
    wandb.log({"responses_collected": len(responses)})

    # Log completion to Prefect
    logger.info(f"✅ Response Simulation Agent completed. Generated {len(responses)} responses.")

    # Convert responses to DataFrame and save to CSV
    df_responses = display_user_responses(responses)
    df_responses.to_csv("df_responses.csv")
    logger.info(f"responses df saved")

    return responses

@flow(name="Agentic Experiment Workflow")
def agentic_experiment_pipeline(product_description: str, num_experiments: int = 1, total_personas: int = 5):
    """
    Main flow that orchestrates the entire A/B testing experiment workflow.
    
    Args:
        product_description (str): Description of the product being tested
        num_experiments (int, optional): Number of experiments to generate. Defaults to 1.
        total_personas (int, optional): Number of user personas to generate. Defaults to 5.
    """
    # Get logger from Prefect
    logger = get_run_logger()
    logger.info("🚀 Starting Agentic Experiment Workflow...")

    # Step 1: Generate experiments
    experiments = run_experiment_agent(num_experiments, product_description)
    
    # Step 2: Generate email campaigns A and B
    email_campaign_a, email_campaign_b = run_email_campaign_agent(experiments)
    
    # Step 3: Generate user personas
    personas = run_persona_agent(email_campaign_a, email_campaign_b, total_personas)

    # Prepare campaigns dictionary for response simulation
    select_campaign = {'A': email_campaign_a, 'B': email_campaign_b}

    # Step 4: Simulate user responses
    user_response = run_response_simulation_agent(personas, select_campaign)

    # Step 5: Generate final report
    run_report_agent(product_description, experiments, email_campaign_a, email_campaign_b, personas, user_response)

    logger.info("✅ Experiment Workflow Completed Successfully, Reports and file present in execution directory!")

if __name__ == "__main__":
    # Initialize Weights & Biases logging
    wandb.login(key=os.environ.get('WANDB_API'))
    wandb.init(project="agentic_experiment", job_type="experiment_tracking")

    # Set up command line argument parser
    parser = ArgumentParser(description="Run workflow with optional number of personas.")
    parser.add_argument('--personas', type=int, default=5, help='Number of personas to use (default: 5)')

    # Parse command line arguments
    args = parser.parse_args()

    # Run the main workflow pipeline with parsed arguments
    agentic_experiment_pipeline(product_description(), num_experiments=1, total_personas=args.personas)
    
    # Finish Weights & Biases logging
    wandb.finish()