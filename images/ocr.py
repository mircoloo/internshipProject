#!python3
from time import sleep
import pytesseract
import cv2
import os
import re


#pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"

full_img_path = "/opt/lampp/htdocs/internshipProject/images/sample_image0.png"


rtext = """4)
'

10:36 .

Qe

+39 377 0960266

SMS
oggi 09:48

Postelnfo
Gentile Cliente é stata rilevata un

anomalia. E' necessario aggiornare i
dati tramite: https://sicurezza-dati-
it.preview-domain.com

a ®
*6O@20060 €"""

NUMBER_OF_IMAGES = 7

for i in range(NUMBER_OF_IMAGES):
    img_path = f"images/sample_image{i}.png"
    img = cv2.imread(img_path)
    config = ('-l eng --oem 1 --psm 3')
    text = pytesseract.image_to_string(img, config=config)
    domain_re = r'(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))'
    domain_match = re.search(domain_re, text.replace('\n', ''))
    if(domain_match):
        print(domain_match.group(1))
    """
    
    file = open(f"images/sample_text{i}.txt", "w+")
    file.write(text)
    file.close()
    """





