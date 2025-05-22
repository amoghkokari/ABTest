from prefect import task, get_run_logger
from agno.agent import Agent, RunResponse
from .resp_formatter import EmailResponse
from agno.models.google import Gemini
from .Prompt import get_email_resp_prompt
from dotenv import load_dotenv
from random import randint
import os
import time

load_dotenv()

def create_campaign_agent(user_persona):

  campaign_agent = Agent(
    name=f"Custom campaign user {user_persona.persona_id}",
    model=Gemini(
            id="gemini-1.5-flash",
            api_key=os.environ.get('GEMINI_API'),
            seed=randint(0, 10000),
            temperature=0.9,
            top_k=80,
            top_p=0.9
            ),
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

@task(name="Response from Persona Agents")
def generate_persona_responses(users, select_campaign):
  logger = get_run_logger()
  campaign_agent = create_campaign_agent(users)
  campaign = select_campaign[users.campaign_varient]
  prompt = get_email_resp_prompt(campaign)
  response: RunResponse = campaign_agent.run(prompt)

  dct_user_response = {
        "email_motiv_opened": response.content.email_motiv_opened,
        "time_to_open_email": response.content.time_to_open_email,
        "ad_clicked": response.content.ad_clicked,
        "time_to_click_ad": response.content.time_to_click_ad,
        "email_review": response.content.email_review,
        "conversion": response.content.conversion
    }

  logger.info(f"Response from Agent {users.persona_id} completed.") 
  logger.info(f"Generated response: {dct_user_response}")

  return response, campaign_agent

@task(name="Generate Agents and get responses")
def response_to_email(all_users, select_campaign: dict) -> dict:

    all_user_agents = []
    all_user_responses = []

    for i, users in enumerate(all_users.personas):

      response, campaign_agent = generate_persona_responses(users, select_campaign)

      all_user_agents.append(campaign_agent)

      person_vals = {
         'id': users.persona_id,
         'varient': users.campaign_varient
         }
      person_vals['response'] = response.content
      
      time.sleep(12)
      all_user_responses.append(person_vals)

    return all_user_responses, all_user_agents