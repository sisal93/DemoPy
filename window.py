import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

try:
    service = Service("C:\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("http://demo.automationtesting.in/Windows.html")
    driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()
    var_win = driver.window_handles

    for handle in var_win:
        print(driver.switch_to.window(handle))
        print(driver.title)

finally:
    time.sleep(3)
    driver.quit()