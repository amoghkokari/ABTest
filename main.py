from helper_func import display_email_campaigns, display_user_personas, display_user_responses, save_as_docx, display_experiment
from agents.email_generator.Agent import generate_email_campaigns_for_experiment
from agents.experiment_generator.Agent import generate_experiments
from agents.response_evaluator.Agent import evaluate_experiment
from agents.response_simulator.Agent import response_to_email
from agents.persona_generator.Agent import generate_personas
from llm_models.AgnoAgentModels import set_api_key
from product_input import product_description
import streamlit as st
import time
import io

def main():
    st.set_page_config(layout="wide")

    # Place this section immediately after st.set_page_config(layout="wide")
    with st.sidebar:
        st.markdown("""
        # What is AI-Driven A/B Testing?
        This application is a **virtual market researcher** that uses Google's Generative AI to simulate a real-world A/B test in seconds, giving you fast, data-driven decisions without needing real customers. 

        ### 1. The Setup: Defining the Test
        You provide a product description. The AI creates a **Hypothesis** (an educated guess about what will work best) and outlines the test goals and the target customer group.

        ### 2. The Creative: Campaigns A vs. B
        Based on the goals, the AI writes two different versions of an email campaign: **Version A** and **Version B**. This is the core of the test—two different approaches to see which performs better.

        ### 3. The Audience: Creating Virtual Testers
        The AI generates a population of **User Personas** (detailed, fictional customer profiles) who perfectly match your target audience. These are your virtual test participants.

        ### 4. The Simulation: Getting Responses
        Each virtual **User Persona** "receives" one of the emails (A or B). The AI simulates how that specific persona would realistically **respond** (e.g., *Would they click? Would they ignore it?*).

        ### 5. The Analysis: The Final Report
        The AI collects all the virtual responses, calculates the performance (like the click-through rate for A vs. B), and generates a detailed **Report**. This report tells you **which version won** and, more importantly, **why**.

        ### 6. The Outcome: Final Download
        Download the complete A/B Test Report as a Word (DOCX) file, ready to share with your team.
        """)

    # App framework setup
    st.title('AI-Driven A/B Testing for Smarter Decision Making')
    st.subheader('Run AI-Powered A/B Testing for Your Product, Just Enter a Description and API Key to Begin!')

    # Input field for selecting sample population size
    st.session_state.num_people = st.number_input("Select the number of participants :", min_value=2, max_value=50, value=6)
    
    # Input field for API key
    api_key = st.text_input('Enter Google Generative AI API KEY (Required)', type="password")
    st.link_button("Click to get API KEY (select create api key in new project)", "https://makersuite.google.com/app/apikey", type="secondary")

    # Use provided API key or fetch from secrets and set it
    api_key = set_api_key(api_key)

    # Initialize session state variables if they don't exist
    if 'resp_content' not in st.session_state:
        st.session_state.resp_content = None
    if 'gen_email_campaign_a' not in st.session_state:
        st.session_state.gen_email_campaign_a = None
    if 'gen_email_campaign_b' not in st.session_state:
        st.session_state.gen_email_campaign_b = None
    if 'users_personas' not in st.session_state:
        st.session_state.users_personas = None
    if 'all_user_responses' not in st.session_state:
        st.session_state.all_user_responses = None
    if 'experiment_valuation' not in st.session_state:
        st.session_state.experiment_valuation = None

    # Reset button to clear all session state variables
    if st.button("Reset Experiment"):
        # Reset all session state variables to None
        st.session_state.resp_content = None
        st.session_state.gen_email_campaign_a = None
        st.session_state.gen_email_campaign_b = None
        st.session_state.users_personas = None
        st.session_state.all_user_responses = None
        st.session_state.experiment_valuation = None

    # Text area for product description input
    with st.expander("Check Product/service description"):
        product_input = st.text_area(label='Type Discription, hit enter after done', placeholder=product_description(), height=300)

    # Use default product description if none provided
    if not product_input:
        product_input = product_description()

    # STEP 1: Generate AB Test Experiment
    if st.button("**1) Generate AB experiment for above desciption**") and api_key and st.session_state.num_people:
        
        # Show status during experiment generation
        with st.status(f"AB experiment creation started by AI agent", expanded=False) as status:
            status.update(
                label=f"Constructing Prompt", state="running", expanded=False
            )
            time.sleep(2)

            status.update(
                label=f"API call to Gemini AI sent", state="running", expanded=False
            )
            # Track time for API call
            start_time = time.time()
            st.session_state.resp_content = generate_experiments(str(1), product_input, api_key)
            end_time = time.time()
            
            ab_elapsed_time = round((end_time - start_time), 2)
            time.sleep(1)
            
            status.update(
                label=f"Response recieved and formatted in {ab_elapsed_time} seconds, click **Experiment Details** to see result", state="complete", expanded=True
            )
    
    if st.session_state.resp_content:

        with st.expander("Experiment details"):

            display_experiment(st.session_state.resp_content)

            # Allow editing of experiment guidelines

            edited_response = st.text_area("Edit Experiment Agent response if needed:", value=st.session_state.resp_content.experiment_guidelines, height=350)
            st.session_state.resp_content.experiment_guidelines = edited_response

    # STEP 2: Generate Email Campaigns for A/B Testing
    if st.session_state.resp_content and st.button("**2) Generate email_campaign A and B**") and api_key:

        # Show status during email campaign generation
        with st.status(f"A and B email generation started by AI agent", expanded=True) as status:
            status.update(
                label=f"Constructing Prompt", state="running", expanded=False
            )
            time.sleep(2)

            status.update(
                label=f"API call to Gemini AI sent", state="running", expanded=False
            )
            # Track time for API call
            start_time = time.time()
            st.session_state.gen_email_campaign_a, st.session_state.gen_email_campaign_b = generate_email_campaigns_for_experiment(st.session_state.resp_content, api_key)
            end_time = time.time()
            
            ab_email_elapsed_time = round((end_time - start_time), 2)
            
            status.update(
                label=f"Response recieved and formatted in {ab_email_elapsed_time} seconds, click **Email Details** to see result", state="complete", expanded=True
            )

    if st.session_state.gen_email_campaign_a and st.session_state.gen_email_campaign_b :

        with st.expander("Email details"):

            # Display email campaigns in a dataframe
            df_email = display_email_campaigns(st.session_state.gen_email_campaign_a, st.session_state.gen_email_campaign_b)

            # Display email table in Streamlit
            st.subheader("AB Test Email Campaigns")
            st.dataframe(df_email[df_email["Attribute"]!="Body"].reset_index(drop=True))
            st.table(df_email[df_email["Attribute"]=="Body"].drop("Attribute", axis = 1).reset_index(drop=True))


            st.session_state.gen_email_campaign_a.variant = st.text_area("Edit campaign A agent response if needed:", 
                                                                         value=st.session_state.gen_email_campaign_a,
                                                                         height=200)

            st.session_state.gen_email_campaign_b.variant = st.text_area("Edit campaign B agent response if needed:", 
                                                                         value=st.session_state.gen_email_campaign_b,
                                                                         height=200)

            # Provide download option for email campaigns
            st.download_button(
                label="**Download emails as CSV**",
                data=df_email.to_csv().encode("utf-8"),
                file_name='email_campaigns_df.csv',
                mime='text/csv',
                icon=":material/download:",
            )

    # STEP 3: Generate User Personas for Testing
    if st.session_state.gen_email_campaign_a and st.session_state.gen_email_campaign_b and st.button("**3) Generate Users Personas**") and st.session_state.num_people and api_key:

        # Show status during user persona generation
        with st.status(f"User Personas Generation started", expanded=True) as status:
            status.update(
                label=f"Constructing Prompt", state="running", expanded=False
            )
            time.sleep(2)

            status.update(
                label=f"API call to Gemini AI sent", state="running", expanded=False
            )
            # Track time for API call
            start_time = time.time()
            st.session_state.users_personas = generate_personas(st.session_state.gen_email_campaign_a.
                                                                target_audience, 
                                                                st.session_state.gen_email_campaign_b.target_audience, 
                                                                st.session_state.num_people,
                                                                api_key)
            end_time = time.time()

            user_persona_elapsed_time = round((end_time - start_time), 2)
            
            status.update(
                label=f"Response recieved and formatted in {user_persona_elapsed_time} seconds, click **Persona Details** to see result", state="complete", expanded=True
            )

    if st.session_state.users_personas:
        df_user_persona = display_user_personas(st.session_state.users_personas)

        with st.expander("Persona details"):
            # Display Persona table in Streamlit
            st.dataframe(df_user_persona)

            # Provide download option for user personas
            st.download_button(
                label="**Download user personas as CSV**",
                data=df_user_persona.to_csv().encode("utf-8"),
                file_name='user_persona_df.csv',
                mime='text/csv',
                icon=":material/download:",
            )

    # STEP 4: Generate User Responses to Email Campaigns
    if st.session_state.users_personas and st.button("**4) Generate Users Responses**") and api_key:

        # Prepare email campaigns for user response simulation
        selected_campaigns = {'A':st.session_state.gen_email_campaign_a, 'B':st.session_state.gen_email_campaign_b}

        # Show status during user response generation
        with st.status(f"AI agents getting Persona responses on emails", expanded=True) as status:
            status.update(
                label=f"Constructing Prompt", state="running", expanded=False
            )
            time.sleep(2)

            status.update(
                label=f"Gathering responses from persona", state="running", expanded=False
            )

            # Initialize lists to store responses and track time
            all_user_responses = []
            total_time_elapsed = 0

            # Generate responses for each user persona
            for i, user in enumerate(st.session_state.users_personas.personas):

                # Track time for each persona's response
                start_time = time.time()
                user_resp, _ = response_to_email(user, selected_campaigns, api_key)
                end_time = time.time()

                all_user_responses.append(user_resp)

                persona_resp_elapsed_time = round((end_time - start_time), 2)

                status.update(
                    label=f"Response recieved for persona {i+1} in {persona_resp_elapsed_time} seconds !!", state="running", expanded=False
                )
                total_time_elapsed += persona_resp_elapsed_time

                # Add delay between API calls to avoid rate limiting
                time.sleep(10)
            
            avg_time_response = round(total_time_elapsed/st.session_state.num_people, 2)

            # Store all user responses in session state
            st.session_state.all_user_responses = all_user_responses
            
            status.update(
                label=f"Response collected and formatted in {total_time_elapsed} seconds or {avg_time_response} seconds per person, click **Persona Responses** to see result", state="complete", expanded=True
            )
    
    if st.session_state.all_user_responses:        

        # Display user responses in a dataframe
        df_user_responses = display_user_responses(st.session_state.all_user_responses)

        with st.expander("Persona Responses"):

            # Display Response table in Streamlit
            st.dataframe(df_user_responses)

            # Provide download option for user responses
            st.download_button(
                label="**Download persona response data as CSV**",
                data=df_user_responses.to_csv().encode("utf-8"),
                file_name='user_response_df.csv',
                mime='text/csv',
                icon=":material/download:",
            )
    
    # STEP 5: Generate AB Test Result Report
    if st.session_state.all_user_responses and st.button("**5) Generate AB Test Report**") and api_key:

        # Show status during user persona generation
        with st.status(f"Test Report Generation started", expanded=True) as status:
            status.update(
                label=f"Constructing Prompt", state="running", expanded=False
            )
            time.sleep(2)

            status.update(
                label=f"API call to Gemini AI sent", state="running", expanded=False
            )

            # Evaluate experiment results based on all collected data
            st.session_state.experiment_valuation = evaluate_experiment(product_input, 
                                                                        st.session_state.resp_content, 
                                                                        st.session_state.gen_email_campaign_a, 
                                                                        st.session_state.gen_email_campaign_b, 
                                                                        st.session_state.users_personas, 
                                                                        st.session_state.all_user_responses, 
                                                                        api_key)
            status.update(
                label=f"Response recieved and formatted, click **Test Report** to see result", state="complete", expanded=True
            )

    if st.session_state.experiment_valuation:

        with st.expander("**AB Test Test Report**"):
            with st.container(height=650):
                # Display sections of the experiment report
                st.markdown("**1. Introduction**")
                st.markdown(st.session_state.experiment_valuation.Introduction)

                # st.markdown("---")
                st.markdown("**2. Experiment Process**")
                st.markdown(st.session_state.experiment_valuation.Experiment_process)
        
                # st.markdown("---")
                st.markdown("**3. Analysis: Campaigns and Personas**")
                tab_campaign, tab_persona = st.tabs(["**Email Campaign Analysis**", "**User Persona & Response**"])

                with tab_campaign:
                    st.markdown("Email Campaign Analysis (A vs. B)")
                    st.markdown(st.session_state.experiment_valuation.Email_Campaign_Analysis)

                with tab_persona:
                    st.markdown("User Persona Analysis & Segmentation")
                    st.markdown(st.session_state.experiment_valuation.User_Persona_Analysis)
                    st.markdown("User Response Analysis (Qualitative)")
                    st.markdown(st.session_state.experiment_valuation.User_Response_Analysis)

                # st.markdown("---")
                st.markdown("**4. Performance Metrics Breakdown**")
                st.markdown(st.session_state.experiment_valuation.Performance_Metrics)

                # st.markdown("---")
                st.markdown("**5. Interpreting the Results & Business Implications**")
                st.markdown(st.session_state.experiment_valuation.Interpretations)

                # st.markdown("---")
                st.markdown("**6. Recommendations for Next Steps**")
                st.markdown(st.session_state.experiment_valuation.Recommendations)

                # st.markdown("---")
                st.markdown("**7. Conclusion**")
                st.markdown(st.session_state.experiment_valuation.Conclusion)
    
    # STEP 6: Save AB Test Report as DOCX
    if st.session_state.experiment_valuation and st.button("**6) Save AB test Result Report**"):

        # Generate DOCX report from experiment valuation
        doc_file = save_as_docx(st.session_state.experiment_valuation, "AB_Test_Report.docx", isWF=False)

        # Create BytesIO object to store document in memory
        bio = io.BytesIO()
        doc_file.save(bio)

        # Provide download button for the DOCX report
        st.download_button(
            label="Click here to download",
            data=bio.getvalue(),
            file_name="AB_Test_Report.docx",
            mime="docx"
        )

    # Author information and links
    st.write("Made with ❤️ by Amogh Mahadev kokari ©️ 2025 _||_ [linkedin](https://www.linkedin.com/in/amoghkokari/) _||_ [Portfolio](https://amoghkokari.github.io/portfolio.pdf) _||_ [Github](https://github.com/amoghkokari)")

# Entry point of the application
if __name__ == "__main__":
    main()