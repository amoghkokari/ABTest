from agno.agent import RunResponse
from general_agents.AgnoAgents import get_agno_agent
from .Prompt import get_experiment_resp_prompt
from .ResponseFormatter import ExperimentResponse


def evaluate_experiment(product_description : str, 
                        experiment_details : str, 
                        email_campaign_a : str, 
                        email_campaign_b : str, 
                        user_personas : str, 
                        user_responses : str, 
                        api_key):
    
    prompt = get_experiment_resp_prompt(product_description, 
                                        experiment_details, 
                                        email_campaign_a, 
                                        email_campaign_b, 
                                        user_personas, 
                                        user_responses)
    evaluator_agent = get_agno_agent(
        response_model=ExperimentResponse,
        instructions="Analyze and follow through the ask in the prompt",
        description="You are an AB test evaluator and report writer expert",
        agent_name="Experiment Evaluator Agent", 
        api_key=api_key,
        goal="follow though the instructions and create the best work based on prompt"
    )

    response: RunResponse = evaluator_agent.run(prompt)

    return response.content