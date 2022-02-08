import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element(By.NAME, "q").send_keys("hello")
time.sleep(3)
driver.save_screenshot("D:\\ScreenShot\\GoogleHome2.png")
time.sleep(2)
driver.get_screenshot_as_file("D:\\ScreenShot\\GoogleHome3.jpeg")
time.sleep(3)
driver.close()