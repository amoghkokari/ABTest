from agno.agent import RunResponse
from general_agents.AgnoAgents import get_agno_agent
from .Prompt import get_a_test_prompt, get_b_test_prompt
from .ResponseFormatter import EmailCampaign

def generate_email_campaigns_for_experiment(experiment: dict, api_key) -> dict:
    
    prompt_a = get_a_test_prompt(experiment)
    email_campaign_agent_a = get_agno_agent(
        response_model=EmailCampaign,
        instructions="Analyze and follow through the ask in the prompt",
        description="You are expert at AB test",
        agent_name="A test Agent", 
        api_key=api_key,
        goal="follow though the instructions and create the best work based on prompt"
        )
    response_a: RunResponse = email_campaign_agent_a.run(prompt_a)

    prompt_b = get_b_test_prompt(experiment, response_a)
    email_campaign_agent_b = get_agno_agent(
        response_model=EmailCampaign,
        instructions="Analyze and follow through the ask in the prompt and make sure it is different from varient A",
        description="You are expert at AB test",
        agent_name="B test Agent", 
        api_key=api_key,
        goal="follow though the instructions and create the best work based on prompt"
    )
    response_b: RunResponse = email_campaign_agent_b.run(prompt_b)

    return response_a.content, response_b.content