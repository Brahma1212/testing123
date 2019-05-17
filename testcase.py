import unittest
from appium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'auto'
        # Returns abs path relative to this file and not cwd
        # desired_caps['app'] = 
os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/Chess 
Free.apk'))
        desired_caps['appPackage'] = 'com.android.chrome'
        desired_caps['appActivity'] = 
'com.google.android.apps.chrome.Main'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', 
desired_caps)

    def test_google_chrome_app(self):
        login_main_page = page.MainPage(self.driver)
        assert login_main_page.click_accept_button()
        assert login_main_page.is_title_matches()
        login_main_page.next_click()
        assert login_main_page.is_title_matches_Signin_Chrome()
        

    def tearDown(self):
        self.driver.close_app()

if __name__ == "__main__":
    unittest.main()
