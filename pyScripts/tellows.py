#!python3
from time import sleep

import selenium
import telGuarder
from telGuarder import *
from selenium.webdriver.common.keys import Keys

def getNumbersFromTelguarder(refreshPage):
    numbers = telGuarder.extractNum(refreshPage)
    return numbers

def searchNumberInformation(num: int):
    tellowsUrl = "https://www.tellows.it/"
    opt = telGuarder.opt
    driver = webdriver.Firefox(options=opt)

    driver.get(tellowsUrl)
    driver.find_element(by=By.CLASS_NAME, value="fc-button-label").click()
    driver.implicitly_wait(3)
    driver.find_element(by=By.ID, value="searchbox-start").clear()
    driver.find_element(by=By.ID, value="searchbox-start").send_keys(num, Keys.ENTER) 
    info = driver.find_element(by=By.ID, value="details").text
    driver.quit()
    return  info

def searchNumbersInformation(driver, numbers: list[int]):  
    for number in numbers:
        try:
            driver.implicitly_wait(5)
            driver.find_element(by=By.ID, value="searchbox-start").clear()
            driver.find_element(by=By.ID, value="searchbox-start").send_keys(number, Keys.ENTER)
            print(number, "\n", driver.find_element(by=By.ID, value="details").text, "\n")
            driver.back()
        except:
            print("Error in searching numbers...")
            driver.quit()    


if __name__ == "__main__":
    """ #for each number search informations on Tellows
    tellowsUrl = "https://www.tellows.it/"

    opt = telGuarder.opt
    driver = webdriver.Firefox(options=opt)
    driver.get(tellowsUrl)
    driver.implicitly_wait(3)

    #accept cookie
    driver.find_element(by=By.CLASS_NAME, value="fc-button-label").click()

    try:
        numbers = getNumbersFromTelguarder(0)
        searchNumbersInformation(driver=driver, numbers=numbers)
    except:
        driver.quit()
    driver.quit() """

    print(searchNumberInformation("0230300659"))


