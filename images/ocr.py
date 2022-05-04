#!python3
from time import sleep
import pytesseract
import cv2
import os


#pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"

full_img_path = "/opt/lampp/htdocs/internshipProject/images/sample_image0.png"


NUMBER_OF_IMAGES = 5

for i in range(NUMBER_OF_IMAGES):
    img_path = f"images/sample_image{i}.png"
    img = cv2.imread(img_path)
    config = ('-l eng --oem 1 --psm 3')
    text = pytesseract.image_to_string(img, config=config)
    file = open(f"images/sample_text{i}.txt", "w+")
    file.write(text)
    file.close()







