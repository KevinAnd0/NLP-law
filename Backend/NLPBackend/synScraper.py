import requests
import re

def get_syn(query):
    response = requests.get(f'https://www.synonymer.se/sv-syn/{query}')
    tags = response.text.split('\n')
    search_tag = '<li value="1"'
    syn_tags = [t for t in tags if search_tag in t]
    syns = re.findall('sv-syn/(.+?)">', syn_tags[0])

    return syns