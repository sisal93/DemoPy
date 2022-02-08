from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

try:
    service = Service("C:\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
    time.sleep(3)

    driver.switch_to.frame("packageListFrame")
    driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
    driver.switch_to.default_content()
    time.sleep(3)

    driver.switch_to.frame("packageFrame")
    driver.find_element(By.LINK_TEXT, "Alert").click()
    driver.switch_to.default_content()
    time.sleep(3)

    driver.switch_to.frame("classFrame")
    driver.find_element(By.LINK_TEXT, "accept").click()
    driver.switch_to.default_content()
    driver.back()
    time.sleep(2)

finally:
    time.sleep(3)
    driver.close()

