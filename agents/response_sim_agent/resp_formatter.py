from pydantic import BaseModel, Field

class EmailResponse(BaseModel):
    email_motiv_opened: str = Field(..., description="email subject motivated you to open or not opinion")
    time_to_open_email: str = Field(..., description="Delta Time in seconds to open the email")
    ad_clicked: str = Field(..., description="ad clicked or not opinion")
    time_to_click_ad: str = Field(..., description="Time in seconds to click the ad")
    email_review: str = Field(..., description="Detailed review response about the email")
    product_review: str = Field(..., description="Detailed review response about the product or service that in email")
    conversion: str = Field(..., description="would you buy the product or service that was advertised in email or not opinion")