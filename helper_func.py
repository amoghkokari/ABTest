from docx import Document
import pandas as pd
import re

def  display_email_campaigns(gen_email_campaign_a, gen_email_campaign_b):
    if gen_email_campaign_a and gen_email_campaign_b:
        # Create a dictionary to format data into a table
        data = {
            "Attribute": ["Variant", "Subject", "Body", "Tone", "Target Audience"],
            "Campaign A": [
                gen_email_campaign_a.variant,
                gen_email_campaign_a.subject,
                gen_email_campaign_a.body,
                gen_email_campaign_a.tone,
                gen_email_campaign_a.target_audience
            ],
            "Campaign B": [
                gen_email_campaign_b.variant,
                gen_email_campaign_b.subject,
                gen_email_campaign_b.body,
                gen_email_campaign_b.tone,
                gen_email_campaign_b.target_audience
            ],
        }

        # Convert to Pandas DataFrame for better table formatting
        return pd.DataFrame(data)
    
def display_user_personas(users):
    dct_user_personas = {
        "persona_id":[],
        "name":[],
        "age":[],
        "gender":[],
        "occupation":[],
        "interests":[],
        "digital_behavior":[],
        "campaign_varient":[]
    }
    for user in users.personas:
        dct_user_personas["persona_id"].append(user.persona_id)
        dct_user_personas["name"].append(user.name)
        dct_user_personas["age"].append(user.age)
        dct_user_personas["gender"].append(user.gender)
        dct_user_personas["occupation"].append(user.occupation)
        dct_user_personas["interests"].append(user.interests)
        dct_user_personas["digital_behavior"].append(user.digital_behavior)
        dct_user_personas["campaign_varient"].append(user.campaign_varient)
    
    return pd.DataFrame(dct_user_personas)

def display_user_responses(responses):
    dct_user_response = {
        "person_id":[],
        "campaign_varient":[],
        "email_motiv_opened":[],
        "time_to_open_email":[],
        "ad_clicked":[],
        "time_to_click_ad":[],
        "email_review":[],
        "conversion":[]
    }

    for resp in responses:
        dct_user_response["person_id"].append(resp["id"])
        dct_user_response["campaign_varient"].append(resp["varient"])
        dct_user_response["email_motiv_opened"].append(resp["response"].email_motiv_opened)
        dct_user_response["time_to_open_email"].append(resp["response"].time_to_open_email)
        dct_user_response["ad_clicked"].append(resp["response"].ad_clicked)
        dct_user_response["time_to_click_ad"].append(resp["response"].time_to_click_ad)
        dct_user_response["email_review"].append(resp["response"].email_review)
        dct_user_response["conversion"].append(resp["response"].conversion)
    
    return pd.DataFrame(dct_user_response)

def save_as_docx(dct_text, filename, isWF=False):
    doc = Document()
    doc.add_heading("AB Test Report", level=1)

    doc.add_heading("Introduction", level=2)
    para = dct_text.Introduction.replace('\n', ' ')
    para = re.sub(' +', ' ', para)
    doc.add_paragraph(para)

    doc.add_heading("Experiment Deep Dive", level=2)
    para = dct_text.Experiment_process.replace('\n', ' ')
    para = re.sub(' +', ' ', para)
    doc.add_paragraph(para)

    doc.add_heading("Email Campaign Analysis", level=2)
    para = dct_text.Email_Campaign_Analysis.replace('\n', ' ')
    para = re.sub(' +', ' ', para)
    doc.add_paragraph(para)

    doc.add_heading("User Persona Analysis", level=2)
    para = dct_text.User_Persona_Analysis.replace('\n', ' ')
    para = re.sub(' +', ' ', para)
    doc.add_paragraph(para)

    doc.add_heading("User Response Analysis", level=2)
    para = dct_text.User_Response_Analysis.replace('\n', ' ')
    para = re.sub(' +', ' ', para)
    doc.add_paragraph(para)

    doc.add_heading("Performance Metrics", level=2)
    para = dct_text.Performance_Metrics.replace('\n', ' ')
    para = re.sub(' +', ' ', para)
    doc.add_paragraph(para)

    doc.add_heading("Interpretations", level=2)
    para = dct_text.Interpretations.replace('\n', ' ')
    para = re.sub(' +', ' ', para)
    doc.add_paragraph(para)

    doc.add_heading("Recommendations", level=2)
    para = dct_text.Recommendations.replace('\n', ' ')
    para = re.sub(' +', ' ', para)
    doc.add_paragraph(para)

    doc.add_heading("Conclusion", level=2)
    para = dct_text.Conclusion.replace('\n', ' ')
    para = re.sub(' +', ' ', para)
    doc.add_paragraph(para)

    if isWF:
        doc.save(filename)

    return doc
