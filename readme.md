🧪 AI-Driven A/B Testing Platform
End-To-End platform to design, simulate, and analyze A/B testing experiments using Generative AI. Perfect for marketers, product teams, startups, and researchers who want to test ideas quickly — without needing real users or heavy data science work.

🚀 Features
-   ✅ Generate A/B testing experiments based on your product description
-   📧 Automatically write two email campaigns (A and B) using AI
-   👥 Simulate user personas for testing based on your target audience
-   📨 Collect simulated user responses to each email variant
-   📊 Get a full experiment analysis report with actionable recommendations
-   📄 Export everything (emails, personas, responses, and reports) as CSV or DOCX

🔍 Use Cases
-   Product messaging testing
-   Marketing copy evaluation
-   UX and behavior research
-   Startup product-market fit validation

🛠️ Tech Stack
-   Frontend: Streamlit
-   Backend: Python
-   AI Models: Google Generative AI (Gemini API)

Others: Pandas, dotenv, io, custom agents using Agno (phiData) for generation and evaluation, Prefect for workflow pipeline automation

🧠 How It Works
1.   Enter a product description
2.   Choose number of AI personas (e.g., 10–50)
3.   Provide your Gemini API Key or set it in environment
4.   Click through 
-   ✅ Generate experiment
-   ✉️ Generate email campaigns
-   👤 Generate user personas
-   📬 Generate user responses
-   📈 Generate A/B test analysis report
5.   Download the results (CSV or DOCX)

🧪 Sample Output
-   📧 A/B Emails: `email_campaigns_df.csv`
-   👤 Personas: `user_persona_df.csv`
-   📬 Responses: `user_response_df.csv`
-   📄 Final Report: `AB_Test_Report.docx`

🔑 Getting Started
1. Clone the repository
    -   `git clone https://github.com/amoghkokari/ABTest.git`
    -   `cd ABTest`
2. Install dependencies
    -   `pip install -r requirements.txt`
3. Create `.streamlit/secrets.toml` file to save keys 
    -   GEMINI_API='<\your api key if you want\>'
    -   GEMINI_VERSION='should be current model version' eg 'gemini-2.5-flash'
4. Run the app
    -   `streamlit run main.py`
5. To run the workflow:
-   Ensure Prefect server is running
    -   on seprate terminal run `prefect server start`
    -   on main terminal run `python workFlow.py`

🔗 Get Your Gemini API Key
-   You can get your API key from Google MakerSuite. Select "Create API key in new project".

</details>
❤️ Built By
Amogh Mahadev Kokari
</details>

📄 License
This project is licensed under the MIT License — feel free to use and adapt!