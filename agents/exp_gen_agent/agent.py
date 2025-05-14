from llm_models.agno_agent_models import get_free_google_model
from agno.agent import Agent, RunResponse
from .resp_formatter import Experiment
from .prompt import get_exp_prompt

experiment_agent = Agent(
    name="Experiment Agent",
    model=get_free_google_model(),
    description ="You are an AB test campaign manager",
    instructions='Analyze and follow through the ask in the prompt',
    goal="follow though the instructions and create the best work based on prompt",
    response_model=Experiment,
    stream=True,
    structured_outputs=True,
    show_tool_calls=True,
    debug_mode=True,
    telemetry=True,
    monitoring=True
)

def generate_experiments(num_experiments: str, product_description: str):
    prompt = get_exp_prompt(num_experiments, product_description)
    response: RunResponse = experiment_agent.run(prompt)
    return response.content