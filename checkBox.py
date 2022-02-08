import timer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
try:
    service = Service("C:\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
    print( "hello")

    driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr[1]/td/label').click()

    driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr[3]/td/label').click()

    driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr[6]/td/label').click()




finally:
    time.sleep(3)
    driver.close()
