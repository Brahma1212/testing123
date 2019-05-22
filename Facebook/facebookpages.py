from facebooklocators import MainPagelocators

class SearchTextElement():
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. facebook.com"""

    #Declares a variable that will contain the retrieved text
    #search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "facebook" appears in page title"""
        return "Facebook" in self.driver.title
    def email(self, username):
        '''Go and finds email id'''
        element = self.driver.find_element(*MainPagelocators.EMAIL)
        if element:
            element.clear()
            element.send_keys(username)
			
    def password(self, userpassword):
        '''Go and finds password id'''
        element = self.driver.find_element(*MainPageLocators.PASSWORD)
        if element:
            element.clear()
            element.send_keys(userpassword)
			
    def login(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN)
        if element:
            element.click()
			
			

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
		
		