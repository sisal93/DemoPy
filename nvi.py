from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

try:
    service = Service("C:\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://humanloop2.nvda.ai/ui/segmentlabeler/jobs/00302754-37bb-11ec-aa05-476f3eb80c27")
    driver.maximize_window()

    for i in range(100):
        driver.find_element(By.XPATH, '//*[@id="shell"]/nv-labeling/div/div[4]/nv-videoplayer/div/div[2]/div[1]/button['
                                      '4]/span[1]/mat-icon').click()

finally:
    time.sleep(3)
    driver.close()
