from appium.webdriver.common.mobileby import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    ACCEPT_BUTTON = (By.ID, "com.android.chrome:id/terms_accept")
    SAVE_DATA = (By.XPATH, "//android.widget.TextView[@text='Save data and browse faster']")
    NEXT_BUTTON = (By.ID,"com.android.chrome:id/next_button")
    SIGN_IN_CHROME = (By.XPATH, "//android.widget.TextView[@text='Sign in to Chrome']")
	

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass
