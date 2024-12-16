from selenium.webdriver.common.by import By

class LoginRegisterPageLocators:
    # Locators for the Login and Register pages of the Book Store Application
    # Locators are combined by the element type

    # The below locators are the same for both pages
    LBL_USERNAME = (By.ID, 'userName-label')
    LBL_PASSWORD = (By.ID, 'password-label')
    LBL_REQ_FLD_EMPTY = (By.CLASS_NAME, 'mr-sm-2 is-invalid form-control')
    INPUT_USERNAME = (By.ID, 'userName')
    INPUT_PASSWORD = (By.ID, 'password')
    CHKBX_REG_RECAPTCHA = (By.ID, 'recaptcha-anchor')

    # The below locators are specific for each page. Locators for the Login page have the LOGIN prefix,
    # locators for the Register page have the REG prefix
    LBL_REG_FIRST_NAME = (By.ID, 'firstname-label')
    LBL_REG_LAST_NAME = (By.ID, 'lastname-label')

    INPUT_REG_FIRST_NAME = (By.ID, 'firstname')
    INPUT_REG_LAST_NAME = (By.ID, 'lastname')

    BTN_LOGIN_LOGIN = (By.ID, 'login')
    BTN_LOGIN_NEW_USER = (By.ID, 'newUser')
    BTN_REG_BACK_TO_LOGIN = (By.ID, 'gotologin')
    BTN_REG_REGISTER = (By.ID, 'register')

