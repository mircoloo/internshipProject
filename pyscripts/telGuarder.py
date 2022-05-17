#!python3
import re
import sys
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import spacy


#retrieve number of refresh from arguments
refresh = 0
if len(sys.argv) == 2:
    refresh = int(sys.argv[1])



def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string

#adding options to firefox driver
opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")

#defining the extract data function -> refreshPage is use to load more numbers retrieving more informations
def extract_data(refreshPage : int = refresh) -> pd.DataFrame:
    telGuarderUrl = "https://www.telguarder.com/it"
    success = True
    #load spacy module 
    nlp = spacy.load('it_core_news_lg')
    #starting telguarder site wait 1 second#
    driver = webdriver.Firefox(options=opt)
    driver.get(telGuarderUrl)


    #accept cookie#
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button")))
    driver.find_element(by=By.ID, value="didomi-notice-agree-button").click()
    
    #refresh the page refresh times
    try:
        for i in range(refreshPage):
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ai-button-rounded")))
            refresh_button = driver.find_element(by=By.CLASS_NAME, value="ai-button-rounded")
            refresh_button.click()

    except:
        print("Error in refreshing the page...")
        success = False
        driver.quit()

    #telephone numbers extraction#
    numbers = []
    try:
        telephonesNumbers = driver.find_elements(by=By.CLASS_NAME, value="ai-phone")#margin-2
        for number in telephonesNumbers:
            if number.text != '':
                numbers.append(number.text)
        del numbers[-20:]
    except:
        print("Error in retrieiving telephone Numbers")
        success = False



    #comments extractions
    comments = []
    organizations = []
    #retrieve all comments

    try:
        numComments = driver.find_elements(by=By.CLASS_NAME, value="ai-column-comment")
    
        for comment in numComments:
            if comment.text != '':
                comment = comment.text[:-36]
                comments.append(comment)
                doc = nlp(comment)
                #retrieve organizaion
                org = ""
                for entity in doc.ents:
                    if(entity.label_ == 'ORG'):
                        org = entity.text
                        break;
                organizations.append(org)
    except:
        print("Error in retrieving comments")
        success = False

    ################################extract and append spam reason##############################
    reasons = []
    try:
        spam_reason = driver.find_elements(by=By.CLASS_NAME,value="ai-spam-reason")
        for reason in spam_reason:
            reasons.append(reason.text)
    except:
        print("Error in retrieving type")
        success = False

    #Extraction number of research and score
    researchs = []
    scores = []
    for num in numbers:
        driver.get("{}/numero/{}".format(telGuarderUrl,num))
        try:
            nSearch = driver.find_element(by=By.CLASS_NAME, value='ai-row-info-value')
            researchs.append(nSearch.text)  
            #try to find score
            try:
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ratingFormOuter")))
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ratingchart")))
                ratingChart = driver.find_element(by=By.ID, value="ratingchart")
                
                """ THIS XPATH SHOULD WORKS BIT IT DOESN'T :') """
                #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='_ABSTRACT_RENDERER_ID_36']/..")))
                """ NOT RACCOMENDED TO USE SLEEP BUT WAS THE ONLY WAY I FOUND THIS SCRIPT TO WORK """
                sleep(3)
                scorePatt = re.compile(r"Negativo\s\((\d+)%\)")
                score = scorePatt.search(ratingChart.text).group(1) 
                dec_score = int(int(score)/10)
                scores.append(dec_score)
            except Exception as e: 
                
                scores.append(4)
                print("score not found, default value is 4") 
        except Exception as e: 
            researchs.append('Not Found')



    #quitting driver
    driver.quit()
    ########BUILDING RELATIONSHIP NUMBER-COMMENT###############
    if success:
        data = []
        for i in range(len(numbers)):
            data.append([numbers[i],comments[i], reasons[i],researchs[i], scores[i] ,"telguarder", organizations[i]])
        df = pd.DataFrame(data, columns=['Number', 'Comment', 'Type', 'Researchs', 'Score', 'Source', 'Organization'])
        return df
    else:
        print('Error in bulding dataFrame: missing informations')
        return None


if __name__ == '__main__':
    print(extract_data())
