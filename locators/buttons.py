from selenium.common import InvalidSelectorException
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By


class ButtonsLocators:

    @staticmethod
    def find_btn_by_label(btn_text: str) -> tuple:
        return (By.XPATH, f'//button[contains(text(), "{btn_text}")]')

    ALERT_BTN = By.ID, 'alertButton'
    TIMER_ALERT_BTN = By.ID, 'timerAlertButton'
    CONFIRM_ALERT_BTN = By.ID, 'confirmButton'
    PROMPT_ALERT_BTN = By.ID, 'promtButton'
    PROGRESS_BAR_BTN = By.ID, 'startStopButton'


class CheckboxesLocators:

    @staticmethod
    def find_checkbox_by_label(label_text: str) -> tuple:
        return By.XPATH, f'//input[contains(@type, "checkbox")]/following-sibling::' \
                         f'span[contains(text(),"{label_text}")]'

    @staticmethod
    def expand_checkbox(label_text: str) -> tuple:
        return By.XPATH, f'//input[contains(@type, "checkbox")]/following-sibling::' \
                        f'span[contains(text(),"{label_text}")]/preceding::button[contains(@title, "Toggle")]'

    @staticmethod
    def get_all_checked():
        return By.XPATH, "//*[name()='svg' and contains(@class, 'rct-icon-check')]/" \
                          f"following::span[contains(@class, 'rct-title')]"

    @staticmethod
    def get_all_halfchecked():
        return By.XPATH, "//*[name()='svg' and contains(@class, 'rct-icon-half-check')]/" \
                         f"following::span[contains(@class, 'rct-title')]"

    @staticmethod
    def is_checkbox_checked(label_text: str) -> tuple:
        try:
            is_checked = By.XPATH, f"//*[name()='svg' and contains(@class, 'rct-icon-check')]/" \
                               f"following::span[contains(@class, 'rct-title') and text() = '{label_text}']"
            return is_checked
        except (InvalidSelectorException, NoSuchElementException):
            pass

    @staticmethod
    def is_checkbox_halfchecked(label_text: str) -> tuple:
        try:
            is_halfchecked = By.XPATH, f"//*[name()='svg' and contains(@class, 'rct-icon-half-check')]/" \
                               f"following::span[contains(@class, 'rct-title') and text() = '{label_text}']"
            return is_halfchecked
        except (InvalidSelectorException, NoSuchElementException):
            pass

    @staticmethod
    def is_checkbox_unchecked(label_text: str) -> tuple:
        try:
            is_unchecked = By.XPATH, f"//*[name()='svg' and contains(@class, 'rct-icon-uncheck')]/" \
                               f"following::span[contains(@class, 'rct-title') and text() = '{label_text}']"
            return is_unchecked
        except (InvalidSelectorException, NoSuchElementException):
            pass

    CHECKBOX_OUTPUT = By.XPATH, "//div[@id='result']/span[text()='You have selected :']/following-sibling::span"
    CHECKBOX_UNCHECKED = By.XPATH, "//*[name()='svg' and contains(@class, 'rct-icon-uncheck')]"
    CHECKBOX_CHECKED = By.XPATH, "//*[name()='svg' and contains(@class, 'rct-icon-check')]"
    CHECKBOX_HALFCHECKED = By.XPATH, "//*[name()='svg' and contains(@class, 'rct-icon-half-check')]"
    CHECKBOX_EXPAND_ALL = By.XPATH, "//button[@aria-label='Expand all']"


class RadiobuttonsLocators:

    @staticmethod
    def find_radiobutton_by_text(radiobtn_text: str) -> tuple:
        return By.XPATH, f'//input[contains(@type, "radio")]/' \
                         f'following-sibling::label[contains(text(), "{radiobtn_text}")]'

    RADIO_RESULT = By.XPATH, '//p[text() = "You have selected "]/span[@class = "text-success"]'
    RADIO_INACTIVE = By.XPATH, '//input[@type="radio" and contains(@class, "disabled")]/following-sibling::label'
