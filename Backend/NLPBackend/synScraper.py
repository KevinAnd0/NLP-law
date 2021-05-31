import requests
import re

def get_syn(query):
    response = requests.get(f'https://www.synonymer.se/sv-syn/{query}')
    search_tags = re.compile(r'<li value="1">(.+?)</li>')
    syn_tags = search_tags.findall(response.text)    
    syns = re.findall('sv-syn/(.+?)">', syn_tags[0])
    return syns
