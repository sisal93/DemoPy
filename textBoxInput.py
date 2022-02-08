import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


try:
    service = Service("C:\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# How to find how many input boxes present in the web page
    text = driver.find_elements(By.CLASS_NAME, 'text_field')
    print(len(text))
    driver.implicitly_wait(2)
# How to provide the values into the text box
    driver.find_element(By.NAME, "RESULT_TextField-1").send_keys("RAM")

    driver.find_element(By.NAME, "RESULT_TextField-2").send_keys("MANI")

    driver.find_element(By.NAME, "RESULT_TextField-3").send_keys("9876543219")

    driver.find_element(By.NAME, "RESULT_TextField-4").send_keys("INDIA")

    driver.find_element(By.NAME, "RESULT_TextField-5").send_keys("AKOLA")

    driver.find_element(By.NAME, "RESULT_TextField-6").send_keys("abc@gmail.com")

finally:
    driver.close()
    print(" ")