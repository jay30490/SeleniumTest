import time

from locators.buttons import ButtonsLocators
from locators.fields import TextFieldsLocators

from modules.base import BasePage


class Alerts(BasePage):

    def accept_alert(self):
        """
        Click OK button on alert

        :return:
        """
        self.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Click Cancel button on alert

        :return:
        """
        self.switch_to.alert.dismiss()

    def prompt_send_text(self, input_text: str):
        """
        Input text to prompt alert

        :param input_text: text to input
        :return:
        """
        prompt = self.switch_to.alert
        time.sleep(1)
        prompt.send_keys(input_text)
        prompt.accept()

    def get_alert_text(self) -> str:
        """
        Get text displayed in alert

        :return: alert text
        """
        alert = self.switch_to.alert
        return alert.text

    def click_alert_btn(self):
        """
        Click button to trigger simple alert

        :return:
        """
        self.find_element(*ButtonsLocators.ALERT_BTN).click()

    def click_confirm_alert_btn(self):
        """
        Click button to trigger confirmation alert

        :return:
        """
        self.find_element(*ButtonsLocators.CONFIRM_ALERT_BTN).click()

    def click_prompt_btn(self):
        """
        Click button to trigger prompt alert

        :return:
        """
        self.find_element(*ButtonsLocators.PROMPT_ALERT_BTN).click()
        time.sleep(1)

    def get_alert_result(self) -> str:
        """
        Get text displayed on the page after making an action with the
        confirmation alert

        :return: text displayed on the page
        """
        return self.find_element(*TextFieldsLocators.ALERT_RESULT).text

    def get_prompt_result(self) -> str:
        """
        Get text displayed on the page after making an action with the
        propmpt alert

        :return: text displayed on the page
        """
        return self.find_element(*TextFieldsLocators.PROMPT_RESULT).text