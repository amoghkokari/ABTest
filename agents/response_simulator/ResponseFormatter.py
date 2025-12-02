from pydantic import BaseModel, Field

class EmailResponse(BaseModel):
    email_motiv_opened: str = Field(
        ..., 
        description="Strictly 'Yes' or 'No'. Your final decision on whether the subject motivated you to open."
    )
    time_to_open_email: int = Field(
        ..., 
        description="Time in seconds (as an integer) it took to open the email after receiving it. Range: 5 to 86400 (1 day)."
    )
    ad_clicked: str = Field(
        ..., 
        description="Strictly 'Yes' or 'No'. Your final decision on whether you clicked the call-to-action link."
    )
    time_to_click_ad: int = Field(
        ..., 
        description="Time in seconds (as an integer) it took to click the ad *after opening the email*. Only return a value > 0 if ad_clicked is 'Yes', otherwise return 0. Range: 0 to 600."
    )
    email_review: str = Field(
        ..., 
        description="A detailed paragraph (3-5 sentences) summarizing your feelings about the email's quality, tone, and effectiveness based on your persona."
    )
    product_review: str = Field(
        ..., 
        description="A detailed paragraph (3-5 sentences) reviewing the product/service itself, considering the advertised features and your persona's needs."
    )
    conversion: str = Field(
        ..., 
        description="Your final decision on whether you would buy/sign up for the product/service advertised. Please prove reason for your action"
    )