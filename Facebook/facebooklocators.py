from selenium.webdriver.common.by import By
class MainPagelocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'pass')
    LOGIN = (By.ID, 'u_0_2')
	

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass