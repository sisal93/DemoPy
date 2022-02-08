from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(3)

element = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/p/span")

action = ActionChains(driver)

action.context_click(element).perform()
time.sleep(3)
driver.close()
