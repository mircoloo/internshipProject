#!python3
import pytesseract
import cv2
import spacy

img = cv2.imread('provaSpacy/image.jpg')


nlp = spacy.load('it_core_news_sm')


# Adding custom options
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)

t = nlp(text)

for token in t:
    print(token, token.morph)

""" cv2.imshow('Immagine 1', img)

cv2.waitKey(0) """