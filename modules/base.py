from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.timeout = 10
        self.action = ActionChains(browser)
