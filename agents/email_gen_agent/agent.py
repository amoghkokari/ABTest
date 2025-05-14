from llm_models.agno_agent_models import get_free_google_model
from agno.agent import Agent, RunResponse
from .prompt import get_a_test_prompt, get_b_test_prompt
from .resp_formatter import EmailCampaign

email_campaign_agent_a = Agent(
    name="A test Agent",
    model=get_free_google_model(),
    description ="You are expert at AB test",
    instructions="Analyze and follow through the ask in the prompt",
    goal="follow though the instructions and create the best work based on prompt",
    response_model=EmailCampaign,
    structured_outputs=True,
    show_tool_calls=True,
    debug_mode=True,
    telemetry=True,
    monitoring=True
)

email_campaign_agent_b = Agent(
    name="B test Agent",
    model=get_free_google_model(),
    description ="You are expert at AB test",
    instructions="Analyze and follow through the ask in the prompt and make sure it is different from varient A",
    goal="follow though the instructions and create the best work based on prompt",
    response_model=EmailCampaign,
    structured_outputs=True,
    show_tool_calls=True,
    debug_mode=True,
    telemetry=True,
    monitoring=True
)

def generate_email_campaigns_for_experiment(experiment: dict) -> dict:
    
    prompt_a = get_a_test_prompt(experiment)
    response_a: RunResponse = email_campaign_agent_a.run(prompt_a)

    prompt_b = get_b_test_prompt(experiment, response_a)
    response_b: RunResponse = email_campaign_agent_b.run(prompt_b)

    return response_a.content, response_b.content