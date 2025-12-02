
def get_experiment_prompt(num_experiments, product_description):
    prompt = (
        f"Generate {num_experiments} detailed experiment for launching a new product. "
        "For each experiment, assign a unique experiment_id, restate the product description, and provide clear, creative experiment guidelines.\n\n"
        "IMPORTANT FORMATTING INSTRUCTIONS:\n"
        "- The 'product_description' and 'experiment_guidelines' fields MUST use Markdown formatting.\n"
        "- Use bullet points (- ), bold text (**text**), and new lines (\\n) to structure the data.\n"
        "- Do not return a solid block of text.\n\n"
        "Generate detailed experiment guidelines based on Product Name and Description provided."
        "Specific Task: Generate AB type email campaigns given a product description.\n"
        f"Product Description: {product_description}"
    )

    return prompt