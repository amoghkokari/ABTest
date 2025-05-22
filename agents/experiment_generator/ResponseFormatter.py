from pydantic import BaseModel, Field

class Experiment(BaseModel):
    experiment_id: str = Field(..., description="Unique experiment identifier")
    product_description: str = Field(..., description="Detailed product description")
    experiment_guidelines: str = Field(..., description="Guidelines for running the experiment")