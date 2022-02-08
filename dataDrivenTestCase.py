import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

import XLUtils

service = Service("C:\\drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://demo.guru99.com/selenium/newtours/")
driver.maximize_window()

# path = "C:\\Users\\Saurabh\\Desktop\\saurabh.xlsx"
#
# rows = XLUtils.getRowCount(path, "Sheet2")
#
# for r in range(2, rows + 1):
#     username = XLUtils.readData(path, "Sheet2", r, 1)
#     password = XLUtils.readData(path, "Sheet2", r, 2)
#     driver.find_element(By.NAME, "userName").send_keys(username)
#     driver.find_element(By.NAME, "password").send_keys(password)
#     driver.find_element(By.NAME, "submit").click()


    # if driver.title == "Welcome: Mercury Tours":
    #     print("test case passed")
    #     XLUtils.writeData(path, "Sheet2", r, 3, "passed")
    # else:
    #     print("test case failed")
    #     XLUtils.writeData(path, "Sheet2", r, 3, "failed")
    # time.sleep(3)
    # driver.find_element(By.LINK_TEXT, "Home").click()
