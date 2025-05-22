from agno.agent import RunResponse
from ..general_agents.AgnoAgents import get_agno_agent
from .Prompt import get_persona_prompt
from .ResponseFormatter import PersonaList


def generate_personas(campaign_a, campaign_b, num_audience: int, api_key):

    prompt = get_persona_prompt(campaign_a, campaign_b, num_audience)
    persona_agent = get_agno_agent(
        response_model=PersonaList,
        instructions="""Generate realistic users based on real world personality for the purpose present in prompt,
                        User should be unique include persona_id, name, age, gender, occupation, a list of interests, description of digital behavior and other asks in prompt""",
        description="You are user reserach professional with expertise in understanding personality of different people",
        agent_name="People personality generator Agent", 
        api_key=api_key,
        goal="follow though the instructions and create the best work based on prompt"
    )

    response: RunResponse = persona_agent.run(prompt, stream=True)

    return response.content