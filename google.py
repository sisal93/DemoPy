from selenium import webdriver
from unittest
try:
    driver = webdriver.Chrome("c:\\drivers\\chromedriver.exe")
    driver.get("https://www.guru99.com/test-plan-v-s-test-strategy.html")
    driver.maximize_window()

finally:
    driver.close()
    print("")
