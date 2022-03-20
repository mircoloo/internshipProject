#!python3
import re
import time
import unicodedata
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#get the recents comments [Number,Comment, Type, Score]

numbers = []
comments = []
types = []
scores = []




opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")  

tellowsUrl = "https://www.tellows.it/"
driver = webdriver.Firefox(options=opt)
driver.implicitly_wait(5)
#driver = webdriver.Firefox()
driver.get(tellowsUrl)


#Accept cookies
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "fc-button-label")))
driver.find_element(by=By.CLASS_NAME, value='fc-button-label').click()

#get recents comments numbers
for i in range(1,7):
    if i == 5: 
        continue
    try: 
        row = driver.find_element(by=By.XPATH, value=f'/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/section/div[9]/ol/li[{str(i)}]/div[1]')
        num_pattern= re.compile(r'[i|I]l\snumero\s(\+?\d+)')
        numero = num_pattern.search(row.text).group(1)
        numbers.append(numero)
    except:
        print(f'Problema nel trovare il {i} commento più recente')

driver.get(tellowsUrl)
for num in numbers:

    try:
        sb = driver.find_element(by=By.ID, value='searchbox')
        sb.clear()
        sb.send_keys(str(num), Keys.ENTER)
        cb = driver.find_element(by=By.CLASS_NAME, value='card-body')
        #print('\n',cb.text, '\n')
         
        
        img = cb.find_element(by=By.CLASS_NAME, value='scoreimage')
        imgText = img.get_attribute('alt')
        description = cb.text
         

        #print("{}\n{}\n{}\n\n".format(num,imgText,description))

        try:
            fComment = driver.find_element(by=By.XPATH, value='//ol[@id="singlecomments"]/li[1]/div[1]/div[2]/p[2]').text
            comments.append(fComment)
            driver.back()                             
        except:
            print('Commento non trovato') 
        #extract informations  
        scorePatt = re.compile(r'Score\s([\d])')
        score = scorePatt.search(imgText).group(1)
        typePatt = re.compile(r'Tipo di chiamata:\s(\w+)')
        type = typePatt.search(description).group(1)


        #build vectors
        types.append(type)      #unicodedata.normalize('NFD', type).encode('ascii', 'ignore'))
        scores.append(score)    
        driver.back() 
    except:
        print('Error...')
        

driver.close()


#build dataFrame
data = []
for i in range(len(numbers)):
    data.append([numbers[i], comments[i], types[i], scores[i]])
df = pd.DataFrame(data, columns=['Number','Comment' ,'Type', 'Score'])

print(df['Comment'])

