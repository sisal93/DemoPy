import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

try:
    service = Service("C:\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

    radio = driver.find_element(By.XPATH,'//*[@id="q26"]/table/tbody/tr[1]/td').is_selected()
    print(radio)
    driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td').click()
    time.sleep(5)
    radio = driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td').is_selected()
    print(radio)
finally:
    print("finally")