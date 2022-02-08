import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_intro")
driver.refresh()
driver.switch_to.frame("iframeResult")

# to find number of rows in table

rows = len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr"))

print("total number of rows are:", rows)

# # to find number of columns in table
cols = len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[1]/th"))
print("total number of columns are: ", cols)

for r in range(2, rows + 1):
    for c in range(1, cols + 1):
        ele = driver.find_element(By.XPATH, "/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").get_attribute("innerHTML")
        print(ele, end="___")

    print()

time.sleep(5)
driver.close()