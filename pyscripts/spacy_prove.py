#!python3 
import spacy
import twitt
from spacy.tokens import DocBin
from tqdm import tqdm
import json 
#df = twitt.extractInformation()

nlp = spacy.load('it_core_news_sm')
db = DocBin()


comm = nlp("ciao")


sent1 = list(comm.sents)[0]
