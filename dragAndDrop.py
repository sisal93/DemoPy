from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

service1 = Service("C:\\drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_element = driver.find_element(By.ID, "box7")
time.sleep(2)
target_element = driver.find_element(By.ID, "box107")

action = ActionChains(driver)

action.drag_and_drop(source_element, target_element).perform()


driver.close()
