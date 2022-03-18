#!python3
import re
import time
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")

driver = webdriver.Firefox(options=opt)
driver.implicitly_wait(15)
driver.get('https://www.tellows.it/num/3486158000')

driver.find_element(by=By.CLASS_NAME, value='fc-button-label').click()

try:
    fComment = driver.find_element(by=By.XPATH, value='//ol[@id="singlecomments"]/li[1]/div[1]/div[2]/p[2]')
            #fComment = driver.find_element(by=By.XPATH,value='/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/section[1]/div[1]/div[7]/ol[1]/li[1]/div[1]/div[2]/p[2]')
    print(fComment.text)
except:
    driver.close()
    print('Error')



driver.close()
