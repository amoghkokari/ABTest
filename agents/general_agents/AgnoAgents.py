from llm_models.AgnoAgentModels import get_free_google_model
from agno.agent import Agent


def get_agno_agent(
        response_model,
        instructions,
        description,
        agent_name, 
        api_key,
        goal,
        structured_outputs=True,
        show_tool_calls=True,
        debug_mode=True,
        telemetry=True,
        monitoring=True,
        ):
    custom_agent = Agent(
        name=agent_name,
        model=get_free_google_model(api_key),
        description=description,
        instructions=instructions,
        goal=goal,
        response_model=response_model,
        stream=True,
        structured_outputs=structured_outputs,
        show_tool_calls=show_tool_calls,
        debug_mode=debug_mode,
        telemetry=telemetry,
        monitoring=monitoring
    )

    return custom_agent