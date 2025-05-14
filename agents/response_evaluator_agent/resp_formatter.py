from pydantic import BaseModel, Field

class ExperimentResponse(BaseModel):
    Introduction: str = Field(..., description="Introduction & Experiment Context")
    Experiment_process: str = Field(..., description="Experiment details")
    Email_Campaign_Analysis: str = Field(..., description="Analysis of Email Campaigns (A vs. B)")
    User_Persona_Analysis: str = Field(..., description="Analysis of User Personas")
    User_Response_Analysis: str = Field(..., description="Analysis of User Responses")
    Performance_Metrics: str = Field(..., description="Performance Metrics Breakdown")
    Interpretations: str = Field(..., description="Interpreting the Results & Business Implications")
    Recommendations: str = Field(..., description="Recommendation for Rollout")
    Conclusion: str = Field(..., description="Final Conclusion and Next Steps")