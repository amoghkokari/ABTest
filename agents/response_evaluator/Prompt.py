
def get_experiment_resp_prompt(product_description, experiment_details, email_campaign_a, email_campaign_b, user_personas, user_responses):
    prompt = (
        "You are An AB test report generator. The experiment used a small sample size for a product.\n"
        f"**Product Description:** {product_description}"
        "\n**Groups:** Variant (A) and Variant (B)\n"
        f"**Experiment Details:** {experiment_details}"
        "\nThe following were tthe two email sent to each group \n"
        f"\n**Email Campaign A:** {email_campaign_a}"
        f"\n**Email Campaign B:** {email_campaign_b}"
        f"\n**Sample Size:** The test was conducted against a limited set of personas (between 2 to 50 divided equally between A and B)."
        f"\n**User Personas:** {user_personas}"
        f"\n**User Responses to emails :** {user_responses}"

        "\nYour response must be a comprehensive report covering the following sections. Given the small sample size (approx. 50), **prioritize qualitative insights and observed trends over strong statistical claims.**\n"

        '''
        1. Introduction 
          contains Introduction & Experiment Context 
        - Provide an overview of the test, why it was conducted, and what was being evaluated.  
        - Explain the key hypothesis.
        - **Crucially, explicitly state the small sample size (6 ot 50 personas) and its implication for the statistical power of the results.**

        2. Experiment_process
          contains detailed process of the experiment describing each steps, what all happened and how each contribute to the success.
          Feel free to add additional details that complement understanding of experiment in depth.

        3. Email_Campaign_Analysis
          contains Analysis of Email Campaigns (A vs. B)
        - Discuss the structure, tone, call-to-action, and content of each email.  
        - Highlight the differences in approach (e.g., emotional appeal, discount offering, subject line variation).  

        4. User_Persona_Analysis 
          contains Analysis of User Personas and Segmentation
        - Compare the two *intended* audience segments and how the **50 personas were distributed and represented** across campaigns A and B.
        - Identify any imbalance or overrepresentation that might bias the simulation.  

        5. User_Response_Analysis 
          contains Analysis of User Responses (Qualitative Focus)
        - Compare how different **persona *types*** reacted to each campaign (e.g., Did 'Feature-Focused' personas respond better to A?).
        - Identify clear qualitative trends in the detailed review fields.
        - Discuss anomalies or unexpected behaviors in the response data.  

        6. Performance_Metrics 
          contains Performance Metrics Breakdown
        - Calculate and **highlight** the observed metrics: Open Rate (A% vs. B%), Click-Through Rate (CTR) (A% vs. B%), and Conversion Rate (A% vs. B%).
        - **IMPORTANT: State clearly that the small sample size (N≈50) means these observed results are indicators, not statistically significant proof.**
        - Instead of *p-value* and *confidence intervals*, calculate and highlight the **Absolute Lift** and **Relative Lift (%)** of the winning variant (if applicable).

        7. Interpretations
          contains Interpreting the Results & Business Implications
        - Based on the observed results and qualitative insights, which campaign (A or B) shows the strongest **INDICATORS** of success?
        - What core insights can we draw from user reviews and motivation fields? 
        - Discuss the limitations imposed by the small sample size.  

        8. Recommendations
          contains Recommendation for Next Steps
        - If Campaign B was better, recommend it for a larger follow-up A/B test.
        - Recommend specific modifications based on the qualitative feedback (e.g., refining subject lines, changing call-to-action).
        - Suggest which persona *type* should be the focus of the next test.

        9. Conclusion
          contains Final Conclusion and Next Steps
        - Summarize the key findings and recommended course of action.  
        - Highlight the most valuable **qualitative insight** gained from this simulation.
        - Reiterate the caveat of the limited sample size.
      ''')

    return prompt