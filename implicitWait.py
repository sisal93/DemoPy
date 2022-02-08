from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

try:
    service = Service("C:\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("http://demo.guru99.com/test/newtours/")
    driver.maximize_window()

    driver.implicitly_wait(3)  # if the web element is not visible then it wait for 3 seconds
    # if web element available before then it execute

    driver.find_element(By.NAME, "userName").send_keys("mercury")
    driver.find_element(By.NAME, "password").send_keys("mercury")
    driver.find_element(By.NAME, "submit").click()


finally:
    driver.close()
