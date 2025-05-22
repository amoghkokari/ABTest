
def get_experiment_prompt(num_experiments, product_description):
    prompt = (
        f"Generate {num_experiments} detailed experiment for launching a new product. "
        "For each experiment, assign a unique experiment_id, restate the product description, and provide clear, creative experiment guidelines."
        "Generate detailed experiment guidelines based on Product Name and Description provided."
        "Generate AB type email campaigns given a product description."
        f"Product Description: {product_description}"
    )

    return prompt