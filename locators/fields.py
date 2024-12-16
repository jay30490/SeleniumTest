from selenium.webdriver.common.by import By


class TextFieldsLocators:

    @staticmethod
    def find_textbox_by_label(label_text: str) -> tuple:
        return By.XPATH, f'//label[contains(text(),"{label_text}")]/parent::div/following-sibling::div/child::input'

    @staticmethod
    def find_textarea_by_label(label_text: str) -> tuple:
        return By.XPATH, f'//label[contains(text(),"{label_text}")]/parent::div/following-sibling::div/child::textarea'

    ERROR_OUTPUT = (By.XPATH, '//input[contains(@class, "field-error")]')
    TEXTBOX_OUTPUT = (By.XPATH, '//div[@id="output"]/descendant::p')
    ALERT_RESULT = By.ID, 'confirmResult'
    PROMPT_RESULT = By.ID, 'promptResult'


class DropDownLocators:

    STATE_LOCATOR = By.XPATH, "//div[text()='Select State']/following-sibling::div/div/input"
    CITY_LOCATOR = By.XPATH, "//div[text()='Select City']/following-sibling::div/div/input"


class DateTimePickerLocators:

    CALENDAR = (By.XPATH, "//div[contains(@class, 'react-datepicker__input-container')]/input")
    MONTH_SELECTOR = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    YEAR_SELECTOR = (By.XPATH, "//select[@class='react-datepicker__year-select']")

    @staticmethod
    def day_selector(day: str):
        return By.XPATH, f"//div[@class='react-datepicker__week']/" \
                         f"div[contains(@class, 'react-datepicker__day') and text() = '{day}']"


class SliderLocators:

    SLIDER = By.XPATH, "//input[@type='range']"
    CURRENT_VALUE_TEXT_BOX = By.ID, 'sliderValue'


class ProgressBarLocators:

    PROGRESS_BAR = By.XPATH, "//div[@id='progressBar']/div"
