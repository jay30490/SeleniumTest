import time

from selenium.webdriver import ActionChains

from locators.buttons import ButtonsLocators
from locators.fields import SliderLocators, ProgressBarLocators
from modules.base import BasePage


class Slider(BasePage):

    def get_slider_min(self) -> str:
        """
        Get minimum value of a slider

        :return: minimum value of a slider
        """
        return self.find_element(*SliderLocators.SLIDER).get_attribute("min")

    def get_slider_max(self) -> str:
        """
        Get maximum value of a slider

        :return: maximum value of a slider
        """
        return self.find_element(*SliderLocators.SLIDER).get_attribute("max")

    def get_current_value(self) -> str:
        """
        Get current value of a slider

        :return: current value of a slider
        """
        return self.find_element(*SliderLocators.SLIDER).get_attribute("value")

    def set_slider_value(self, new_value: int):
        """
        Set a new slider value

        :param new_value: xoffset to be set
        :return:
        """
        sld = self.find_element(*SliderLocators.SLIDER)
        ActionChains(self).drag_and_drop_by_offset(sld, new_value, 0).perform()

    def set_slider_to_mid(self):
        """
        Set slider value to the middle

        :return:
        """
        sld = self.find_element(*SliderLocators.SLIDER)
        ActionChains(self).drag_and_drop_by_offset(sld, 1, 0).perform()
