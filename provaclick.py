#!python3
import re
import time
from numpy import number
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get('https://www.tellows.it/')
driver.implicitly_wait(3)
driver.find_element(by=By.CLASS_NAME, value='fc-button-label').click()
driver.implicitly_wait(3)

lasInserted = driver.find_element(by=By.XPATH, value='/html/body/main/div/div[1]/div[1]/section/div[9]/ol/li[1]/div[1]')
#toClick =lasInserted.find_element(by=By.XPATH, value='div[2]/a')  
toClick =lasInserted.find_element(by=By.CLASS_NAME, value='mb-2')  
time.sleep(4)
try: 
    print(toClick.text)
    toClick.click()
except:
    print('Unclickable')
    driver.quit()




driver.close()
