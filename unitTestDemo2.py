import unittest
import webbrowser

from selenium.webdriver.chrome import webdriver


def test_Google():
    print("this is second method")


class DemoSearch(unittest.TestCase):

    @classmethod
    def setUp(cls):
        print("this is Login")

    @classmethod
    def tearDown(cls):
        print("this is logout ")

    @classmethod
    def setUpClass(cls):
        print("Open the application:::")

    @classmethod
    def tearDownClass(cls):
        print("close the application:::::::")

    def test_Bing(self):
        driver = webdriver.Chrome("c:\\drivers\\chromedriver.exe")
        driver.
        print("this is  first method")


if __name__ == "__main__":
    unittest.main()
