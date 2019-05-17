from locators import MainPageLocators
from appium.webdriver.common.mobileby import By
import time

class MainPage(object):
    """Home page action methods come here. I.e. Python.org"""
	
    def __init__(self, driver):
        self.driver = driver
	
    def click_accept_button(self):
        time.sleep(7)
        element = self.driver.find_element(*MainPageLocators.ACCEPT_BUTTON)
        print("ellement", element)
        if element:
            element.click()
            return True
        else:
            return False

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return self.driver.find_element(*MainPageLocators.SAVE_DATA)

    def is_title_matches_Signin_Chrome(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return self.driver.find_element(*MainPageLocators.SIGN_IN_CHROME)
		
    def next_click(self):
        '''Go and finds email id'''
        element = self.driver.find_element(*MainPageLocators.NEXT_BUTTON)
        if element:
            element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source

