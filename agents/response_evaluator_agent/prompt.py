
def get_experiment_resp_prompt(product_description, experiment_details, email_campaign_a, email_campaign_b, user_personas, user_responses):
    prompt = (
        "You are An AB test report generator, the AB test was created with two groups for a product description\n"
        f"{product_description}"
        "\nGroup (A) and Group (B)\n"
        "Detail of generated Experiment: \n"
        f"{experiment_details}"
        "\nThe following were tthe two email sent to each group \n"
        f"Grop A : {email_campaign_a}"
        f"\nGrop B : {email_campaign_b}"
        "\nThe email were tested againt the following personas: \n"
        f"{user_personas}"
        "\nThese were the responses by the users: \n"
        f"{user_responses}"

        "your response should include the following (highlight numbers wherever possible, keep proper spacing and formatting):\n"

        '''
        1. Introduction 
          contains Introduction & Experiment Context 
        - Provide an overview of the test, why it was conducted, and what was being evaluated.  
        - Explain the key hypothesis
        - Explain the flow of the experiment to merit its novelity

        2. Experiment_process
          contains detailed process of the experiment describing each steps, what all happened and how each contribute to the sucess
          fell free to add additional details that complement understanding of experiment in depth

        3. Email_Campaign_Analysis
          contains Analysis of Email Campaigns (A vs. B)
        - Discuss the structure, tone, call-to-action, and content of each email.  
        - Highlight the differences in approach (e.g., emotional appeal, discount offering, subject line variation).  

        4. User_Persona_Analysis 
          contains Analysis of User Personas and Responses
        - Compare how different user personas are taken into account for each campaign.  
        - Identify trends among the people participated  
        - Discuss anomalies or unexpected users taken into consideration with aim of keep experiment novel.  

        5. User_Response_Analysis 
          contains Analysis of User Responses
        - Compare how different **user personas reacted** to each campaign.  
        - Identify trends: *Did younger users prefer one campaign? Did certain demographics show stronger engagement?*  
        - Discuss anomalies or unexpected behaviors in the response data.  

        6. Performance_Metrics 
          contains Performance Metrics Breakdown
        - Email Open Rate: [A% vs. B%]  
        - Click-Through Rate (CTR): [A% vs. B%]  
        - Conversion Rate: [A% vs. B%]  
        - Engagement Metrics (Time spent, interactions, replies, etc.)  
        - Statistical Significance (Include p-value and confidence intervals)  
        - Effect Size and Lift Analysis (How much better/worse did B perform over A?)  

        7. Interpretations
          contains Interpreting the Results & Business Implications
        - Based on the results, which campaign (A or B or none) is more effective?
        - What insights can we draw from user responses? 
        - Were there any confounding factors? (Seasonality, user bias, sample imbalance)  

        8. Recommendations
          contains Recommendation for Rollout
        - If Campaign B outperformed Campaign A, should it be rolled out to all users?
        - If results were inconclusive, what should be tested next?  
        - What modifications (e.g., refining subject lines, changing call-to-action) can be made for better success?  

        9. Conclusion
          contains Final Conclusion and Next Steps while showing the importance of this study
        - Summarize the key findings and recommended course of action.  
        - Suggest future testing considerations to optimize further.  
        - Highlight any caveats or limitations (e.g., small sample size, external factors).
      ''')

    return prompt