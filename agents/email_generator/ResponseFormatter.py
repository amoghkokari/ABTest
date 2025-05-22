from pydantic import BaseModel, Field

class EmailCampaign(BaseModel):
    variant: str = Field(..., description="Campaign variant (A or B)")
    subject: str = Field(..., description="Email subject line")
    body: str = Field(..., description="Email body copy including product details and a call-to-action")
    tone: str = Field(..., description="Tone of the email (e.g., friendly, professional)")
    target_audience: str = Field(..., description="Description of the intended audience")