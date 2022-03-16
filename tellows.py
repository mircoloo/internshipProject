#!python3
import re
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#get the recents comments [Number,Comment, Type, Score]

opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")  

tellowsUrl = "https://www.tellows.it/"

driver = webdriver.Firefox(options=opt)
#driver = webdriver.Firefox()
driver.get(tellowsUrl)


#Accept cookies
driver.find_element(by=By.CLASS_NAME, value='fc-button-label').click()
driver.implicitly_wait(3)

numbers = []
types = []
comments = []
scores = []

#get recents comments numbers
for i in range(1,7):
    if i == 5: continue
    try:   
        riga = driver.find_element(by=By.XPATH, value=f'/html/body/main/div/div[1]/div[1]/section/div[9]/ol/li[{i}]/div[1]')
        driver.implicitly_wait(3)
        comment = riga.find_element(by=By.CLASS_NAME, value='comment-body').text
        driver.implicitly_wait(3) 
        numPatt = re.compile(r'il\snumero\s(\+?\d+)')
        numero = numPatt.search(comment).group(1)
        """
        patterns = re.compile(r'come\s(\w+\s?[^0-9]+)')
        tipo = patterns.search(comment).group(1)
        types.append(tipo[:-1])
        """
        numbers.append(numero)
        driver.implicitly_wait(3)
    except:
        print("Comment not found\n")



driver.get(tellowsUrl)
for num in numbers:
    try:
        sb = driver.find_element(by=By.ID, value='searchbox')
        sb.clear()
        sb.send_keys(str(num), Keys.ENTER)
        driver.implicitly_wait(3)
        cb = driver.find_element(by=By.CLASS_NAME, value='card-body')
        img = cb.find_element(by=By.CLASS_NAME, value='scoreimage')
        imgText = img.get_attribute('alt')
        scorePatt = re.compile(r'Score\s([\d])')
        scoreVal = scorePatt.search(imgText).group(1)
        text = cb.text
        typePatt = re.compile(r'Tipo di chiamata:\s(\w+\s?\w+)')
        cal_type = typePatt.search(text).group(1)


        #build vectors
        types.append(cal_type)
        scores.append(scoreVal)
        
    except:
        print(f'Qualcosa con ricerca di {num} è andato storto')

driver.close()

data = []
for i in range(len(numbers)):
    data.append([numbers[i], types[i], scores[i]])
df = pd.DataFrame(data, columns=['Number', 'Type', 'Score'])

print(df)


