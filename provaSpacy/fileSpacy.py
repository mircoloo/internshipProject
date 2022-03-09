#!python3
import spacy



nlp = spacy.load('it_core_news_sm')

#text = "A Mirco piace partecipare a questo progetto delegato da FBK in quanto non sta capendo nulla di quello che sta facendo. Gli piace programmare in diversi linguaggi, studia ingegneria informatica e spera di laurearsi a breve"
text = open('tweets.txt', 'r').read()

doc = nlp(text) 



for token in doc:
    print(token.ent_type_)
    


