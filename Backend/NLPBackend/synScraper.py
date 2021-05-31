import requests
import re

def get_syn(query):
    response = requests.get(f'https://www.synonymer.se/sv-syn/{query}')
    syn_tags = re.findall(r'<li value="1">(.+?)</li>', response.text)    
    syns = re.findall(r'sv-syn/(.+?)">', syn_tags[0])
    return syns
