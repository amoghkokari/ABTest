def get_email_resp_prompt(campaign):
    prompt = (
        "You are the persona defined in the instructions, and you have received the following email in your mailbox."
        "Your objective is to go through the email and provide opinions based on your personality, interests, and digital behavior."
        
        "\n### Email Content to Review:"
        f"**Subject:** {campaign.subject}\n"
        f"**Body:** {campaign.body}\n"
        f"**Tone:** {campaign.tone}\n"
        
        "\n### Task and Constraints:"
        "You open ALL emails, but your subsequent actions and opinions are **highly individualized** based on your persona."
        
        "Your response MUST strictly adhere to the required JSON structure and include the following simulated actions and opinions:"
        "- **Motivation:** Whether the subject motivated you to open it (Yes/No) and why."
        "- **Time to Open (Seconds):** A simulated time it took to open the email (an integer value)."
        "- **Ad Clicked:** Whether you clicked the ad (Yes/No) and why."
        "- **Time to Click (Seconds):** A simulated time it took to click the ad *after opening* (an integer). Return **0** if the ad was not clicked."
        "- **Email Review:** A detailed review of the email's quality."
        "- **Product Review:** A detailed review of the product/service."
        "- **Conversion:** Your final decision on whether you would buy the product (Yes/No) and why."
    )
    return prompt