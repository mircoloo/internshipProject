#!python3 
import spacy
import twitt
from spacy.tokens import DocBin
from tqdm import tqdm
import json 
#df = twitt.extractInformation()
# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load('it_core_news_lg')

# Process whole documents
text = ("""16:22 ~- B aE

<SMS truffa in circolazione.

ATTENZIONE A QUESTI SMS!

Avviso la sua APP UniCredit
risulta associata ad un dispositivo
da Lugano se non sei tu bloccalo

a link https://is.gd./UnicreditSpa

ATTENZIONE: un dispositivo

non autorizzato ci risulta connesso
al suo conto online se disconosce
tale accesso clicca i] modulo
correlato

Gentile cliente il suo supporto
tecnico é l’operatore n 4321
Mario Rossi dell’Ufficio Antifrode

Gentile cliente la sua utenza é
sospesa a causa frode, a breve
sara contattato da un nostro
operatore dell’ufficio sicurezza
""")


doc = nlp(text)

# Analyze syntax
#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])



# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)