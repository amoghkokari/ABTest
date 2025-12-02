def get_persona_prompt(campaign_a_audience: str, campaign_b_audience: str, num_personas: int = 1000):
    """
    Generates a prompt to create diverse personas strictly aligned with two specified campaign audiences.
    """
    prompt = (
        f"Generate {num_personas} distinct user personalities for a new digital product launch. "
        "The personas must be strictly categorized into two target audiences for an A/B test. "

        f"**Target Audience A Description (Map to campaign_varient='A'):** '{campaign_a_audience}' "
        f"**Target Audience B Description (Map to campaign_varient='B'):** '{campaign_b_audience}' "
        
        f"Ensure you generate AT MOST an equal balance between the two classes (A and B). "
        
        "For each persona, the 'digital_behavior' field must **explain why this user is a good fit for the product described by their assigned campaign variant (A or B)**, linking their habits to the product's need. "
        
        "Include all required fields: persona_id (unique string), name, age, gender, occupation, a list of interests, detailed digital behavior, and the assigned campaign_varient ('A' or 'B')."
        f"Ensure the total count is exactly {num_personas} unique personas."
    )

    return prompt