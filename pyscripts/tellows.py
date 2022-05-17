#!python3
import re
import time
import unicodedata
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import spacy



def extract_data():
    nlp = spacy.load('it_core_news_lg')
    #get the recents comments [Number,Comment, Type, Researchs, Score, Organization]
    numbers = []
    comments = []
    types = []
    researchs = []
    scores = []
    organizations = []

    #adding arguments to Firefox options in order to avoid the opening of the windows 
    opt = webdriver.FirefoxOptions()
    opt.add_argument("--headless")  
    tellowsUrl = "https://www.tellows.it/"
    driver = webdriver.Firefox(options=opt)
    driver.get(tellowsUrl)
    success = True

    #Accept cookies scripts 
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "fc-button-label")))
        driver.find_element(by=By.CLASS_NAME, value='fc-button-label').click()
    except:
        print('Error in cookie accept')
        success = False

    #iterate for all the 5 recent comments and retrieve the numbers 
    count = 0
    for i in range(1,7):
        count += 1
        if i == 5: 
            continue
        try: 
            row_text = driver.find_element(by=By.XPATH, value='(//ol[@id="singlecomments"])[2]/li[{}]/div[1]/div[2]/p[1]'.format(i)).text
            num_pattern= re.compile(r'[i|I]l\snumero\s(\+?\d+)')  
            num = num_pattern.search(row_text).group(1)
            numbers.append(num)
            success = True
        except:
            #driver.close()
            print("Probem in retrieving the {} number".format(count))
            success = False

    #iterate for all the 5 numbers and retrieve the | comment | type | score informations
    for num in numbers:
        try:
            #search the web page of any number
            driver.get(f"{tellowsUrl}/num/{num}")
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "card-body")))

            #find the card board and the score image and retrieve the attribute alt in order to obtain the score later
            card_board = driver.find_element(by=By.CLASS_NAME, value='card-body')
            score_img = card_board.find_element(by=By.CLASS_NAME, value='scoreimage')
            img_text = score_img.get_attribute('alt')
            description = card_board.text
            

            #find the first comment of the number and extract organizations if present
            try:
                first_Comment = driver.find_element(by=By.XPATH, value='//ol[@id="singlecomments"]//div[@class="col comment-body"]/p[2]').text
                comments.append(first_Comment)
                doc = nlp(first_Comment)
                org = ""
                for entity in doc.ents:
                    if(entity.label_ == 'ORG'):
                        org = entity.text
                        break;
                driver.back()                             
            except:
                print('Comment not found')
                success = False
            #extract score, researchs and type from the text
            try: 
                scorePatt = re.compile(r"Score\s([\d])")
                score = scorePatt.search(img_text).group(1)
                typePatt = re.compile(r"Tipo di chiamata:\s(.*)")
                #typePatt = re.compile(r"Tipo di chiamata:\s(\w+)")
                type = typePatt.search(description).group(1)
                #retreive number od researchs, if present
                try:
                    researchsPatt = re.compile(r"Ricerche:\s(\d+)")
                    research = researchsPatt.search(description).group(1)
                except:
                    research = "-1"
                    pass
                
                
            except:
                print('Error in retrieving information form text: Regex error')
                success = False

            #build vectors of type | score | 
            types.append(type)      #unicodedata.normalize('NFD', type).encode('ascii', 'ignore'))
            scores.append(score)    
            researchs.append(research)
            organizations.append(org)

            driver.back()  
        except:
            print('Error in retrieving informations from the number: {}'.format(num))
            success = False

    #close the firefox driver       
    driver.close()
    #list of number data 
    data = []


    #if all the steps goes succesfully
    if success:
        #build dataFrame
        print("Building dataFrame...")
        for i in range(len(numbers)):
            data.append([numbers[i], comments[i], types[i],researchs[i],scores[i], "tellows", organizations[i]])
            df = pd.DataFrame(data, columns=['Number','Comment' ,'Type','Researchs','Score', 'Source', 'Organization'])
        #print(df)
        return df
    else:
        print('Error in building dataFrame: missing informations')
        return None

if __name__ == '__main__':
    print(extract_data())