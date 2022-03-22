#!python3
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string


opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")


def extract_data(refreshPage: int = 0):
    telGuarderUrl = "https://www.telguarder.com/it"

    #starting telguarder site wait 1 second#
    driver = webdriver.Firefox(options=opt)
    driver.implicitly_wait(10)
    driver.get(telGuarderUrl)


    #accept cookie#
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button")))
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
        search_bar = driver.find_element(by=By.ID, value='queryInput')
        search_bar.clear()
        search_bar.send_keys(str(num), Keys.ENTER)
        try:
            nSearch = driver.find_element(by=By.CLASS_NAME, value='ai-row-info-value')
            researchs.append(nSearch.text)
            driver.back()
        except:
            researchs.append('ND')
            

    
    ########BUILDING RELATIONSHIP NUMBER-COMMENT#
    data = []
    for i in range(len(numbers)):
        data.append([numbers[i],comments[i], reasons[i],researchs[i]])
    driver.quit()
    df = pd.DataFrame(data, columns=['Number', 'Comment', 'Type', 'Researchs'])
    return df

if __name__ == '__main__':
    print(extract_data(1))
