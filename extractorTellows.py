#!python3
from time import sleep
import extractorTelGuarder
from extractorTelGuarder import *
from selenium.webdriver.common.keys import Keys

def getNumbersFromTelguarder(refreshPage):
    numbers = extractorTelGuarder.extractNum(refreshPage)
    return numbers


#for each number search informations on Tellows
tellowsUrl = "https://www.tellows.it/"

opt = extractorTelGuarder.opt
driver = webdriver.Firefox(options=opt)
driver.get(tellowsUrl)
driver.implicitly_wait(3)

#accept cookie
driver.find_element(by=By.CLASS_NAME, value="fc-button-label").click()

#for each number search information
numbers = extractNum(1)
sleep(1)
for number in numbers:
    try:
        driver.implicitly_wait(1)
        driver.find_element(by=By.ID, value="searchbox-start").clear()
        driver.find_element(by=By.ID, value="searchbox-start").send_keys(number, Keys.ENTER)
        print(number, "\n", driver.find_element(by=By.ID, value="details").text, "\n")
        driver.back()
    except:
        driver.quit()    


