from llm_models.agno_agent_models import get_free_google_model
from agno.agent import Agent, RunResponse
from .resp_formatter import EmailResponse
from .prompt import get_email_resp_prompt
import time

def create_campaign_agent(user_persona):

  campaign_agent = Agent(
    name=f"Custom campaign user {user_persona.persona_id}",
    model=get_free_google_model(),
    description ="You are user an user with the following personality properties"
                f"name: {user_persona.name}"
                f"age: {user_persona.age}"
                f"gender: {user_persona.gender}"
                f"occupation: {user_persona.occupation}"
                f"interests: {user_persona.interests}"
                f"digital_behavior: {user_persona.digital_behavior}",
    instructions="Generate realistic users based responses for the prompt based on who you are"
                "Remember yourself and what you are while responding to prompt",
    goal="follow though the instructions and create the best work based on prompt",
    response_model=EmailResponse,
    structured_outputs=True,
    show_tool_calls=True,
    debug_mode=True,
    telemetry=True,
    monitoring=True
  )

  return campaign_agent

def response_to_email(user, select_campaign: dict) -> dict:
  
  campaign_agent = create_campaign_agent(user)
  campaign = select_campaign[user.campaign_varient]

  prompt = get_email_resp_prompt(campaign)

  response: RunResponse = campaign_agent.run(prompt)

  person_vals = {
    'id': user.persona_id,
    'varient': user.campaign_varient
  }
  
  person_vals['response'] = response.content
  
  return person_vals, campaign_agent
