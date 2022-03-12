#!python3
import pytesseract
import cv2
import time
import spacy

img = cv2.imread('image.jpg')

nlp = spacy.load('it_core_news_sm')


# Adding custom options
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)
print(img)
print(text)

t = nlp(text)

cv2.imshow('Immagine 1', img)

cv2.waitKey(0)