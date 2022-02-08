
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

try:
    service = Service("C:\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("http://demo.guru99.com/test/newtours/")
    driver.maximize_window()

# to count total numbers of links in web page
    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"There are total {len(links)} links")
# to print all links in terminal

    for i in links:
        print(i.text)

# to click on particular link in web page

    driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()


finally:
    time.sleep(3)
    driver.close()
