from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium import webdriver

try:
    service = Service("C:\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("http://testautomationpractice.blogspot.com/")
    driver.maximize_window()

    driver.switch_to.frame("frame-one1434677811")
    var_path = "C://Users/Saurabh/Pictures/Fact-Dimension-Model.jpg"
    driver.find_element(By.NAME, "RESULT_FileUpload-10").send_keys(var_path)
finally:
    print(" ")
