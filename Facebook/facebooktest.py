import unittest
import time
from selenium import webdriver
from facebookpages import MainPage
class Facebooksearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Users\Admin\Desktop\python pro\chromedriver")
        self.driver.get("http://www.facebook.com")

    def main_Facebookpage(self):
		login_main_page = page.FacebookPage(self.driver)
		assert login_main_page.is_title_matches(), "facebook.com title doesn't match."
		login_main_Facebookpage.email("jbreddy517@gmail.com")
		login_main_Facebookpage.password("Mother@123")
		login_main_Facebookpage.login()
    time.sleep(10)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()