from agno.agent import RunResponse
from ..general_agents.AgnoAgents import get_agno_agent
from .Prompt import get_email_resp_prompt
from .ResponseFormatter import EmailResponse

def create_campaign_agent(user_persona, api_key):

  campaign_agent = get_agno_agent(
    response_model=EmailResponse,
        # instructions="""Generate realistic users based responses for the prompt based on who you are",
        #         Remember yourself and what you are while responding to prompt""",
        instructions="""Generate realistic user responses for the email prompt.
                You must strictly adhere to the structured output model. 
                Your opinions, clicks, times, and conversion decisions MUST be logically consistent with your assigned persona and the specific email content.""",
        description ="""You are user an user with the following personality properties" 
                f"name: {user_persona.name}" 
                f"age: {user_persona.age}" 
                f"gender: {user_persona.gender}" 
                f"occupation: {user_persona.occupation}" 
                f"interests: {user_persona.interests}" 
                f"digital_behavior: {user_persona.digital_behavior}""",
        agent_name=f"Custom campaign user {user_persona.persona_id}", 
        api_key=api_key,
        goal="Generate a highly realistic user interaction with an email advertisement based on the defined persona."
        # goal="follow though the instructions and create the best work based on prompt"
  )

  return campaign_agent

def response_to_email(user, select_campaign: dict, api_key) -> dict:
  
  campaign_agent = create_campaign_agent(user, api_key)
  campaign = select_campaign[user.campaign_varient]

  prompt = get_email_resp_prompt(campaign)

  response: RunResponse = campaign_agent.run(prompt)

  person_vals = {
    'id': user.persona_id,
    'varient': user.campaign_varient
  }
  
  person_vals['response'] = response.content
  
  return person_vals, campaign_agent
