from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com/")
double = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')

action = ActionChains(driver)

action.double_click(double).perform()

