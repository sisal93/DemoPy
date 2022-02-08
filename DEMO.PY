from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then
#invoke actual browser
driver = webdriver.Chrome()
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.google.com/")
#to refresh the browser
driver.refresh()
driver.switch_to.frame("iframeResult")
# identifying the header from row1 having <th> tag
cols = driver.find_element("/html/body/table/tbody/tr")
# len method is used to get the size of that list
print(len(cols))
#to close the browser
driver.close()