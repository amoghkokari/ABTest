
def get_persona_prompt(campaign_a, campaign_b, num_audience: int = 1000):
    prompt = (
        f"Generate {num_audience} distinct user personalities for a new digital product launch."
        f"Target audiences are: '{campaign_a}' and '{campaign_b}'. Ensure you atmost balance both classes"
        "Include persona_id, name, age, gender, occupation, interests, digital behavior, campaign_varient for each persona."
        "Ensure each persona_id is unique."
        f"Ensure you have {num_audience} many different personas"
    )

    return prompt