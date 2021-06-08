import requests
import re
from google_trans_new import google_translator
# import spacy

# nlp = spacy.load(r"C:\SISTA PROJEKT ARBETE\sv_pipeline-0.0.0\sv_pipeline-0.0.0\sv_pipeline\sv_pipeline-0.0.0")



# def keyword_ext(query):
#     pos_tag = ['NOUN']
#     doc = nlp(query.lower())
#     for d in doc:
#         if(d.is_stop or d.is_punct):
#             continue
#         if(d.pos_ in pos_tag):
#             return d.text

def id_language(query):
    detector = google_translator()  
    detect_lang = detector.detect({query})
     
    return detect_lang            


def get_syn(query):
    # if id_language(query) != "sv":
    #     translator = google_translator()
    #     query = translator.translate(query, lang_tgt="sv")
        
    response = requests.get(f'https://www.synonymer.se/sv-syn/{query}')
    syn_tags = re.findall(r'<li value="1">(.+?)</li>', response.text)    
    syns = re.findall(r'sv-syn/(.+?)">', syn_tags[0])
    syns.insert(0, query)
    return syns
    

