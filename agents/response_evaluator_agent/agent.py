from llm_models.agno_agent_models import get_free_google_model
from agno.agent import Agent, RunResponse
from .resp_formatter import ExperimentResponse
from .prompt import get_experiment_resp_prompt

evaluator_agent = Agent(
    name="Experiment Agent",
    model=get_free_google_model(),
    description ="You are an AB test evaluator and report writer expert",
    instructions='Analyze and follow through the ask in the prompt',
    goal="follow though the instructions and create the best work based on prompt",
    response_model=ExperimentResponse,
    stream=True,
    structured_outputs=True,
    show_tool_calls=True,
    debug_mode=True,
    telemetry=True,
    monitoring=True
)

def evaluate_experiment(product_description : str, experiment_details : str, email_campaign_a : str, email_campaign_b : str, user_personas : str, user_responses : str):
    prompt = get_experiment_resp_prompt(product_description, experiment_details, email_campaign_a, email_campaign_b, user_personas, user_responses)
    response: RunResponse = evaluator_agent.run(prompt)
    return response.content