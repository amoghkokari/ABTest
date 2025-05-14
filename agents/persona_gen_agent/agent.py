from llm_models.agno_agent_models import get_free_google_model
from agno.agent import Agent, RunResponse
from .resp_formatter import PersonaList
from .prompt import get_persona_prompt

persona_agent = Agent(
    name="People personality generator Agent",
    model=get_free_google_model(),
    description ="You are user reserach professional with expertise in understanding personality of different people",
    instructions="Generate realistic users based on real world personality for the purpose present in prompt"
                "User should be unique include persona_id, name, age, gender, occupation, a list of interests, description of digital behavior and other asks in prompt",
    goal="follow though the instructions and create the best work based on prompt",
    update_knowledge=True,
    response_model=PersonaList,
    structured_outputs=True,
    show_tool_calls=True,
    debug_mode=True,
    telemetry=True,
    monitoring=True
)

def generate_personas(campaign_a, campaign_b, num_audience: int = 1000) :
    prompt = get_persona_prompt(campaign_a, campaign_b, num_audience)
    response: RunResponse = persona_agent.run(prompt, stream=True)

    return response.content