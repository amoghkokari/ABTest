from pydantic import BaseModel, Field
from typing import List

class Persona(BaseModel):
    campaign_varient: str = Field(
        ..., 
        description="Campaign variant, must be strictly 'A' or 'B', based on the prompt's audience description."
    )
    persona_id: str = Field(
        ..., 
        description="A unique string identifier for the persona (e.g., 'VG_A_001')."
    )
    name: str = Field(..., description="A realistic full name.")
    age: int = Field(..., description="Age, must be a realistic integer between 18 and 80.")
    gender: str = Field(..., description="Gender (e.g., Male, Female, Non-Binary).")
    occupation: str = Field(..., description="Detailed current occupation.")
    interests: List[str] = Field(
        ..., 
        description="A list of 3-5 specific interests relevant to the digital product or wellness/tech space."
    )
    digital_behavior: str = Field(
        ..., 
        description="A detailed description (2-3 sentences) of this person's online habits, focusing on **why they are a target for the assigned campaign variant (A or B)**."
    )

class PersonaList(BaseModel):
    # Field added to ensure the LLM provides all items as a list under this key
    personas: List[Persona] = Field(..., description="A list containing all generated user personas.")