
def get_email_resp_prompt(campaign):
    prompt = (
        f"You are sent the following email in your mailbox, your objective is to go through the email provide the following response\n"
        f"tone of email: {campaign.tone}"
        f"Subject: {campaign.subject}\n"
        f"Body: {campaign.body}\n"
        "you open all the email and very individualistic with your opinions\n"
        "your response should include:\n"
        "- Whether the email subject motivated you to open it or not and why\n"
        "- Delta Time to open after the email was recieved (in seconds)\n"
        "- Whether you clicked the ad or not and why\n"
        "- Time to click the ad (in seconds)\n"
        "- A detailed review text response about the email\n"
        "- A detailed review text response about the product or service that in email\n"
        "- Did you buy the product or service that was advertised in the email or not and why"
      )

    return prompt