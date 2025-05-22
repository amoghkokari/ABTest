from pydantic import BaseModel, Field
from typing import List

class Persona(BaseModel):
    campaign_varient: str = Field(..., description="Campaign variant (A or B)")
    persona_id: str = Field(..., description="Unique persona identifier")
    name: str = Field(..., description="Name")
    age: int = Field(..., description="Age")
    gender: str = Field(..., description="Gender")
    occupation: str = Field(..., description="Occupation")
    interests: List[str] = Field(..., description="Interests")
    digital_behavior: str = Field(..., description="Digital behavior description")

class PersonaList(BaseModel):
    personas: List[Persona]