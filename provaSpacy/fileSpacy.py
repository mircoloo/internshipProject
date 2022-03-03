#!python3

from cv2 import DescriptorMatcher
import spacy



nlp = spacy.load("it_core_news_sm")

with open("/Users/mircobisoffi/Desktop/acaso.txt", "r") as f:
    text = f.read()

doc = nlp(text) 

sentence1 = list(doc.sents)

for sent in list(doc.sents)[:5] :
    for token in sent:
        #if(token.ent_type == )
        print(token, token.ent_type_)