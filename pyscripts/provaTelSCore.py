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


opt = webdriver.FirefoxOptions()
opt.add_argument("--headless")

#defining the extract data function -> refreshPage is use to load more numbers retrieving more informations

telGuarderUrl = "https://www.telguarder.com/it/numero/3515261447"
#starting telguarder site wait 1 second#
driver = webdriver.Firefox(options=opt)
#driver = webdriver.Firefox()
driver.get(telGuarderUrl)
driver.implicitly_wait(10)


#accept cookie#
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button")))
driver.find_element(by=By.ID, value="didomi-notice-agree-button").click()

try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ratingFormOuter")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ratingchart")))
    ratingChart = driver.find_element(by=By.ID, value="ratingchart")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "_ABSTRACT_RENDERER_ID_4")))
    print(ratingChart.text)
    scorePatt = re.compile(r"Negativo\s\((\d+)%\)")
    score = scorePatt.search(ratingChart.text).group(1) 
    print(score)
except Exception as e:
    print(e)

driver.close()