from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.fields import DateTimePickerLocators

from modules.base import BasePage


class Calendar(BasePage):

    def open_calendar(self):
        self.find_element(*DateTimePickerLocators.CALENDAR).click()

    def close_calendar(self):
        pass

    def input_date(self, month: str, year: str, day: str):
        self.find_element(*DateTimePickerLocators.CALENDAR).click()
        WebDriverWait(self, 3).until(
            EC.visibility_of_element_located(DateTimePickerLocators.MONTH_SELECTOR))
        # self.wait_visibility(DateTimePickerLocators.MONTH_SELECTOR)
        month_sel = Select(self.find_element(*DateTimePickerLocators.MONTH_SELECTOR))
        month_sel.select_by_visible_text(month)
        year_sel = Select(self.find_element(*DateTimePickerLocators.YEAR_SELECTOR))
        year_sel.select_by_visible_text(year)
        self.find_element(*DateTimePickerLocators.day_selector(day)).click()


