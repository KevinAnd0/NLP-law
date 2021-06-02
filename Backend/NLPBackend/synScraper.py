import requests
import re
# import spacy

# nlp = spacy.load(r"E:\Coding\nlpmodel\sv_pipeline-0.0.0\sv_pipeline\sv_pipeline-0.0.0")

# def noun_ex(query):
#     pos_tag = ['NOUN']
#     doc = nlp(query.lower())
#     for d in doc:
#     #     print(d.text, d.pos_)
#         if(d.is_stop or d.is_punct):
#             continue
#         if(d.pos_ in pos_tag):
#             return d.text

def get_syn(query):
    # keyword = keyword_ext(query)
    response = requests.get(f'https://www.synonymer.se/sv-syn/{query}')
    syn_tags = re.findall(r'<li value="1">(.+?)</li>', response.text)    
    syns = re.findall(r'sv-syn/(.+?)">', syn_tags[0])
    return syns
