import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# to download file on specific location
opt1 = Options()
opt1.add_experimental_option("prefs", {"download.default_dictionary": "C:\\Users"})

driver = webdriver.Chrome(options=opt1)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
# to download text file

driver.find_element(By.ID, "textbox").send_keys("This is Automation Practice Code made by Saurabh isal")
driver.find_element(By.ID, "createTxt").click()
driver.find_element(By.ID, "link-to-download").click()
# to download pdf file
# pdf not open properly its have some problem
driver.find_element(By.ID, "pdfbox").send_keys("This is Automation Practice Code made by Saurabh isal")
driver.find_element(By.ID, "createPdf").click()
driver.find_element(By.ID, "pdf-link-to-download").click()
