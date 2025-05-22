from agno.agent import RunResponse
from ..general_agents.AgnoAgents import get_agno_agent
from .Prompt import get_experiment_prompt
from .ResponseFormatter import Experiment


def generate_experiments(num_experiments: str, product_description: str, api_key):

    prompt = get_experiment_prompt(num_experiments, product_description)
    experiment_agent = get_agno_agent(
        response_model=Experiment,
        instructions="Analyze and follow through the ask in the prompt",
        description="You are an AB test campaign manager",
        agent_name="Experiment Agent", 
        api_key=api_key,
        goal="follow though the instructions and create the best work based on prompt"
        )
    response: RunResponse = experiment_agent.run(prompt)

    return response.content