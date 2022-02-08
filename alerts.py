from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time

try:
    service = Service("C:\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("http://testautomationpractice.blogspot.com/")

    driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()
    time.sleep(2)
# to click on the ok button in alert pop up message
    driver.switch_to.alert.accept()
    time.sleep(3)
# to click on the cancel button in alert pop up message
    driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()
    time.sleep(2)
    driver.switch_to.alert.dismiss()

finally:
    driver.quit()
    print("finally executed")
