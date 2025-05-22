
def get_a_test_prompt(experiment):
    prompt = (
        f"Based on the following experiment guidelines: {experiment.experiment_guidelines}, "
        f"generate email campaign for A variant (of A and B) for a newly launched product, product description: {experiment.product_description} . "
        "write email For each variant A, provide a subject line, detailed email body with a clear call-to-action, tone, and target audience."
    )

    return prompt

def get_b_test_prompt(experiment, earlier_response):
    prompt = (
        f"Based on the following experiment guidelines: {experiment.experiment_guidelines}, "
        f"generate email campaign for B variant (of A and B) for a newly launched product, product description: {experiment.product_description} . "
        "write separate email For each variant B, provide a subject line, detailed email body with a clear call-to-action, tone, and target audience."
        f"Please make sure the subject, body, tone and target_audience is different from A varient {earlier_response.content}"
    )

    return prompt