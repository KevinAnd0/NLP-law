import os
import io
from pdfminer.high_level import extract_text
import re
import spacy
from heapq import nlargest

dir_path = os.getcwd()
path_to_pdfs = rf'{dir_path}\test_pdf_reader'
path_to_pipeline = rf'{dir_path}\sv_pipeline-0.0.0\sv_pipeline\sv_pipeline-0.0.0'
nlp=spacy.load(path_to_pipeline)

list_of_pdfs = os.listdir(path_to_pdfs)

def summarize(file_name):
    text = preprocess_text(file_name)
    doc = nlp(text)

    word_frequencies = {}
    for token in doc:
        if not (token.is_punct or token.is_stop or token.text == "\n"):
            if token.text.lower() not in word_frequencies.keys():
                word_frequencies[token.text.lower()] = 1
            else:
                word_frequencies[token.text.lower()] += 1
    
    max_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    sentence_tokens = [token.sent for token in doc if token.is_sent_start]

    sentence_scores = {}
    for sent in sentence_tokens:
        # Remove sentences with too many words
        if len(sent.text.split(' ')) > 50:
          continue    
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    select_length = 3
    summary = nlargest(select_length, sentence_scores, sentence_scores.get)
    summary = [token.text for token in summary]
    summary = ' '.join(summary)
    summary = summary.replace('\n', ' ')
    return summary


def getIndexes(domstol, text):
    index_start = 0
    index_end = 0
    word_start = ''

    if domstol == 'Marknadsdomstolen':

        if text.find("\nBakgrund\n") != -1:
            word_start = "\nBakgrund\n"

        elif text.find("\nBAKGRUND\n") != -1:
            word_start = "\nBAKGRUND\n"

        elif text.find("\nGRUNDER OCH UTVECKLING AV TALAN\n") != -1:
            word_start = "\nGRUNDER OCH UTVECKLING AV TALAN\n"

        elif text.find("\nMARKNADSDOMSTOLENS AVGÖRANDE\n") != -1:
            word_start = "\nMARKNADSDOMSTOLENS AVGÖRANDE\n"

        elif text.find("\nGRUNDER\n") != -1:
            word_start = "\nGRUNDER\n"
     
        index_start = text.find(word_start)

        word_end = "\nRättegångskostnader\n"
        index_end = text.find(word_end)

        if index_end == -1:
            word_end = "På Marknadsdomstolens vägnar\n"
            index_end = text.find(word_end)
    
    elif 'högsta' in domstol.lower() or 'hovrätt' in domstol.lower():
         word_start = "\nREFERAT\n"
         index_start = text.find(word_start)

         word_end = "Sökord:"
         index_end = text.find(word_end)


    elif domstol == 'Arbetsdomstolen':
        word_start = "\nBakgrund\n"
        index_start = text.find(word_start)
        if index_start == -1:
            word_start = "\nBAKGRUND\n"
            index_start = text.find(word_start)

        word_end = "\nDOMSLUT\n"
        index_end = text.find(word_end)


    elif domstol == 'Miljööverdomstolen':

        if text.find("\nYRKANDEN M.M. I MILJÖÖVERDOMSTOLEN\n") != -1: 
            word_start = "\nYRKANDEN M.M. I MILJÖÖVERDOMSTOLEN\n"
        elif text.find("\nYRKANDEN M.M.\n") != -1: 
            word_start = "\nYRKANDEN M.M.\n"
        elif text.find("\nYRKANDEN I MILJÖÖVERDOMSTOLEN\n") != -1:
            word_start = "\nYRKANDEN I MILJÖÖVERDOMSTOLEN\n"
        
        index_start = text.find(word_start)

        word_end = "\nHUR MAN ÖVERKLAGAR, se bilaga"
        index_end = text.find(word_end)


    elif 'Mark-' in domstol:

        if text.find("\nUTVECKLING AV TALAN I MARK- OCH MILJÖÖVERDOMSTOLEN\n") != -1: 
            word_start = "\nUTVECKLING AV TALAN I MARK- OCH MILJÖÖVERDOMSTOLEN\n"
        elif text.find("\nUTVECKLANDE AV TALAN I MARK- OCH MILJÖÖVERDOMSTOLEN\n") != -1: 
            word_start = "\nUTVECKLANDE AV TALAN I MARK- OCH MILJÖÖVERDOMSTOLEN\n"
        
        index_start = text.find(word_start)

        word_end = "\nHUR MAN ÖVERKLAGAR, se bilaga"
        index_end = text.find(word_end)

    return [index_start, index_end, len(word_start)]        


def preprocess_text(file_name):

    text = extract_text(fr'{path_to_pdfs}/{file_name}')
    text = '\n\n' + text

    # Get the the type of court, which always is always in the top of the text.
    text_temp = re.sub(r'\n\n\S+(?=\n\n)', '', text)
    text_temp = text_temp.lstrip()
    domstol = text_temp[:text_temp.find('\n')].replace(' ', '')

    indexes = getIndexes(domstol, text)

    index_start = indexes[0]
    index_end = indexes[1]
    start_word_length = indexes[2]

    text = text[index_start + start_word_length: index_end]
    return text