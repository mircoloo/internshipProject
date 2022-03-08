#!python3

from spacy import displacy
import spacy



nlp = spacy.load("it_core_news_sm")

text = "A Mirco piace partecipare a questo progetto delegato da FBK in quanto non sta capendo nulla di quello che sta facendo."

doc = nlp(text) 



for token in doc:
    print(token.text, token.pos_, token.dep_, token.lemma_)
    


