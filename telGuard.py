#!python3
from click import option
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")


def extractNumData(refreshPage: int):
    telGuarderUrl = "https://www.telguarder.com/it"

    #starting telguarder site wait 1 second#
    driver = webdriver.Firefox(options=opt)
    driver.get(telGuarderUrl)


    #accept cookie#
    acceptCookie = driver.find_element(by=By.ID, value="didomi-notice-agree-button").click()
    try:
        for i in range(refreshPage):
            button = driver.find_element(by=By.CLASS_NAME, value="ai-button-rounded")
            button.click()
            driver.implicitly_wait(1)
    except:
        print("non trovato")
        driver.quit()


    #telephone numbers extraction#
    numbers = []
    telephonesNumbers = driver.find_elements(by=By.CLASS_NAME, value="ai-phone")#margin-2
    for number in telephonesNumbers:
        if number.text != '':
            "//table[@class, 'test']/tbody.." 
            numbers.append(number.text)
    del numbers[-20:]



    #comments extractions
    comments = []
    numComments = driver.find_elements(by=By.CLASS_NAME, value="ai-column-comment")
    for comment in numComments:
        if comment.text != '':
            cleanedComment = comment.text.removesuffix("\nCommento dell'utente (Italia,  web)")
            cleanedComment = cleanedComment.removesuffix("\nCommento dell'utente (Italia,  app)")
            comments.append(cleanedComment)


    #spam reason
    reasons = []
    spam_reason = driver.find_elements(by=By.CLASS_NAME,value="ai-spam-reason")
    for reason in spam_reason:
        reasons.append(reason.text)


    #Extraction number of research
    driver.get(telGuarderUrl)
    researchs = []
    for num in numbers:
        searchBar = driver.find_element(by=By.ID, value='queryInput')
        searchBar.clear()
        searchBar.send_keys(str(num), Keys.ENTER)
        driver.implicitly_wait(1)
        try:
            nSearch = driver.find_element(by=By.CLASS_NAME, value='ai-row-info-value')
            #print(nSearch.text)
            researchs.append(nSearch.text)
            driver.back()
            driver.implicitly_wait(1)
        except:
            #print(num,"Num non trovato")
            researchs.append('Not found')
            

    
    ########BUILDING RELATIONSHIP NUMBER-COMMENT#
    numCom = []
    for i in range(len(numbers)):
        numCom.append([numbers[i],comments[i], reasons[i],researchs[i]])
    driver.quit()
    return numCom


data = extractNumData(2)
df = pd.DataFrame(data, columns=['Number', 'Comment', 'Reason','Researchs'])
print(df)