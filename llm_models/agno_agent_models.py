from agno.models.google import Gemini
from dotenv import load_dotenv
import os

load_dotenv()

def get_free_google_model():
    return Gemini(
        id=os.environ.get('GEMINI_VERSION'),
        api_key=os.environ.get('GEMINI_API')
    )

def get_free_google_model_w_parameters(seed_val=142, temperature_val=0.9, top_k_val=.09, top_p_val=0.9):
    return Gemini(
        id=os.environ.get('GEMINI_VERSION'),
        api_key=os.environ.get('GEMINI_API'),
        seed=seed_val,
        temperature=temperature_val,
        top_k=top_k_val,
        top_p=top_p_val
    )