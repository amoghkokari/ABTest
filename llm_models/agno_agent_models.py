from agno.models.google import Gemini
from dotenv import load_dotenv
import os

load_dotenv()

def get_free_google_model():
    return Gemini(
        id=os.environ.get('GEMINI_VERSION'),
        api_key=os.environ.get('GEMINI_API')
    )

# from random import randint
#     model=Gemini(
#             id="gemini-1.5-flash",
#             api_key=os.environ.get('GEMINI_API'),
#             seed=randint(0, 10000),
#             temperature=0.9,
#             top_k=80,
#             top_p=0.9
#             ),