import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.NAME, "Submit").click()

admin = driver.find_element(By.XPATH, '//*[@id="menu_admin_viewAdminModule"]/b')
usermang = driver.find_element(By.XPATH, '//*[@id="menu_admin_UserManagement"]')
user = driver.find_element(By.XPATH, '//*[@id="menu_admin_viewSystemUsers"]')

action = ActionChains(driver)
action.move_to_element(admin).move_to_element(usermang).move_to_element(user).click().perform()

time.sleep(3)
driver.close()