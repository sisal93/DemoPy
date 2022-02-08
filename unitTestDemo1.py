import time
import unittest
from selenium import webdriver


class SearchEngine(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        time.sleep(3)

    def test_Bing(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.bing.com/")
        time.sleep(3)

    def test_Opera(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.opera.com")

        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
