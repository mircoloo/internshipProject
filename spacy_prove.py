#!python3 
import spacy
import twitt


#df = twitt.extractInformation()

nlp = spacy.load('it_core_news_sm')

text = open('commento.txt', 'r').read()

comm = nlp(text)


sent1 = list(comm.sents)[0]


for tok in sent1:
    print(tok.text,tok.dep_)




