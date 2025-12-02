def get_a_test_prompt(experiment):
    prompt = (
        f"Based on the following experiment guidelines: {experiment.experiment_guidelines}, "
        f"generate the email campaign for Variant A for a newly launched product, product description: {experiment.product_description}. "
        "Provide a subject line, detailed email body, clear call-to-action (CTA) text, tone, and target audience. "
        "**Crucially, format the email body using Markdown (newlines, bullet points, bolding) for clarity.**"
    )
    return prompt

def get_b_test_prompt(experiment, earlier_response):
    prompt = (
        f"Based on the following experiment guidelines: {experiment.experiment_guidelines}, "
        f"generate the alternative email campaign for Variant B for a newly launched product, product description: {experiment.product_description}. "
        "Provide a subject line, detailed email body, clear call-to-action (CTA) text, tone, and target audience. "
        "**Crucially, format the email body using Markdown (newlines, bullet points, bolding) for clarity.**"
        f"Ensure the subject, body, tone, CTA, and target audience are distinctly different from Variant A: {earlier_response.content}"
    )
    return prompt