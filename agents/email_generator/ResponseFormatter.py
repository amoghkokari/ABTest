from pydantic import BaseModel, Field

class EmailCampaign(BaseModel):
    variant: str = Field(..., description="Campaign variant (e.g., A or B).")
    subject: str = Field(..., description="Email subject line.")
    body: str = Field(
        ..., 
        description="Detailed email body, formatted using Markdown for readability (newlines, bullet points, bolding). DO NOT include the CTA button text here."
    )
    call_to_action: str = Field(..., description="The main call-to-action (CTA) text (e.g., 'Download Now' or 'Learn More').")
    tone: str = Field(..., description="Overall tone of the email (e.g., 'Feature-Focused and Direct' or 'Benefit-Driven and Empathetic').")
    target_audience: str = Field(..., description="A concise description of the specific segment targeted.")