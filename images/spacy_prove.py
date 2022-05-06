#!python3 
import spacy
import json 
#df = twitt.extractInformation()
# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load('it_core_news_lg')
#nlp = spacy.load('en_core_web_lg')

# Process whole documents
text = open("images/sample_text3.txt", "r").read()
text = """
        Truffa sms di Poste Italiane. Analisi di un altro caso di phishing - Matrice Digitale #cybercrime #evidenza #posteinfo #truffa  https://t.co/c941znepRo
        """
organizations = ['UNICREDIT', 'POSTEID', 'POSTEINFO', 'POSTEPAY', 'BANCAMPS', 'N26', 'INTESA']


doc = nlp(text)

# Analyze syntax
#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

print("\n--------------------------\n")



# Find named entities, phrases and concepts
for entity in doc.ents:
    if(entity.label_ == 'ORG'):
        print(entity)
    #print(entity.text, entity.label_)
    
""" 
for keyword in organizations:
    if(keyword in text.upper()):
        print("presente ", keyword)
        exit()
    else:
        print("organizzazione non presente")  """