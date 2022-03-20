#!python3
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string


opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")


def extractNumData(refreshPage: int):
    telGuarderUrl = "https://www.telguarder.com/it"

    #starting telguarder site wait 1 second#
    driver = webdriver.Firefox(options=opt)
    driver.implicitly_wait(30)
    driver.get(telGuarderUrl)


    #accept cookie#
    acceptCookie = driver.find_element(by=By.ID, value="didomi-notice-agree-button").click()
    try:
        for i in range(refreshPage):
            button = driver.find_element(by=By.CLASS_NAME, value="ai-button-rounded").click()
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
            cleanedComment = remove_suffix(comment.text, "\nCommento dell'utente (Italia,  web)")
            cleanedComment = remove_suffix(cleanedComment, "\nCommento dell'utente (Italia,  app)")
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
        try:
            nSearch = driver.find_element(by=By.CLASS_NAME, value='ai-row-info-value')
            #print(nSearch.text)
            researchs.append(nSearch.text)
            driver.back()
        except:
            #print(num,"Num non trovato")
            researchs.append('ND')
            

    
    ########BUILDING RELATIONSHIP NUMBER-COMMENT#
    numCom = []
    for i in range(len(numbers)):
        numCom.append([numbers[i],comments[i], reasons[i],researchs[i]])
    driver.quit()
    df = pd.DataFrame(numCom, columns=['Number', 'Comment', 'Type', 'Researchs'])
    return df

if __name__ == '__main__':
    
    print(extr)
    

