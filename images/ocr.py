#!python3
import pytesseract
import cv2
import os


#pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"

img_path = "sample_image2.png"

img = cv2.imread(img_path)

cv2.imshow("image", img)

""" config = ('-l eng --oem 1 --psm 3')
text = pytesseract.image_to_string(img, config=config)
print(img) """







