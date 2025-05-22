from agno.models.google import Gemini
# from dotenv import load_dotenv
from streamlit import secrets

# load_dotenv()

# AIzaSyDolrFGbWlYwsc3PNkCPkY_5b8qpQqsg9I

def set_api_key(api_key):
    
    api_key = api_key if api_key else secrets["GEMINI_API"] # replace with "os.environ.get('GEMINI_API')" to use .env

    return api_key

def get_free_google_model(ai_api_key):
   
    return Gemini(
        id=secrets["GEMINI_VERSION"], # replace with "os.environ.get('GEMINI_VERSION')" to use .env
        api_key=ai_api_key
    )

def get_free_google_model_w_parameters(ai_api_key,
                                       seed_val=142, 
                                       temperature_val=0.9, 
                                       top_k_val=.09, 
                                       top_p_val=0.9):

    return Gemini(
        id=secrets["GEMINI_VERSION"], # replace with "os.environ.get('GEMINI_VERSION')" to use .env
        api_key=ai_api_key,
        seed=seed_val,
        temperature=temperature_val,
        top_k=top_k_val,
        top_p=top_p_val
    )