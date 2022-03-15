#!python3
import re
from time import sleep
from click import option
from numpy import number
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#get the recents comments [Number,Comment, Type, Score]

opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")  

tellowsUrl = "https://www.tellows.it/"

driver = webdriver.Firefox(options=opt)
driver.get(tellowsUrl)


#Accept cookies
driver.find_element(by=By.CLASS_NAME, value='fc-button-label').click()
driver.implicitly_wait(3)

"""
righe = driver.find_elements(by=By.CLASS_NAME, value='row')
for r in righe:
    try:
        print(r.find_element(by=By.CLASS_NAME, value='comment-body').text)
    except:
        print('commento non trovato')
"""
numbers = []

#recent comments
for i in range(1,7):
    try:
        riga = driver.find_element(by=By.XPATH, value=f'/html/body/main/div/div[1]/div[1]/section/div[9]/ol[1]/li[{i}]/div[1]')
        comment = riga.find_element(by=By.CLASS_NAME, value='comment-body').text
        #riga.find_element(by=By.CLASS_NAME, value='btn').text)
        t = "ocr ha segnalato Sconosciuto con il numero +393482764328 come Truffa 15/03/22 14.00 Avevano il mio numero ma cercavano mia madre per la bolletta della luce, molto molto sospetto. Appena ho chiesto come avessero il mio numero hanno attaccato 6 Valutazioni per +393482764328 (Vodafone (cellulare))"
        pattern = re.compile(r'il\snumero\s\+?(\d{7,15})')
        numero = pattern.search(comment).group(1)
        numbers.append(numero)

    except:
        print("Comment not found\n")
driver.close()


print(numbers)