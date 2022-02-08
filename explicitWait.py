import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

try:
    service = Service("C:\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.expedia.co.in/")

    driver.find_element(By.XPATH, "//*[@id='wizardMainRegion']/div[1]/div/div/div/div/ul/li[2]/a/span").click()
    # driver.find_element(By.XPATH, "//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[1]/div/div/div/button").click()
    driver.find_element(By.XPATH, '//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[1]/div/div[1]/div/div/div/button').click()
finally:

    print("finally done")
