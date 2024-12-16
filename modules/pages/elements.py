import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys

from locators.fields import TextFieldsLocators
from locators.buttons import ButtonsLocators
from locators.buttons import CheckboxesLocators
from locators.buttons import RadiobuttonsLocators
from locators.fields import DropDownLocators

from modules.base import BasePage


class FieldsInput(BasePage):

    def find_textfield_by_label(self, label_text: str):
        """
        Set cursor on a text field with the specified label text

        :param label_text: text of the label specified next to a text field
        :return:
        """
        self.find_element(*TextFieldsLocators.find_textbox_by_label(label_text)).click()

    def clear_textfield_by_label(self, label_text: str):
        """
        Clear the text field with the specified label text

        :param label_text: text of the label specified next to a text field
        :return:
        """
        fld = self.find_element(*TextFieldsLocators.find_textbox_by_label(label_text))
        fld.click()
        fld.clear()

    def input_text(self, label_text: str, input_text: str = ""):
        """
        Enter text into the text field with the specified label text

        :param label_text: text of the label specified next to a text field
        :param input_text: text to be entered
        :return:
        """
        fld_input = self.find_element(*TextFieldsLocators.find_textbox_by_label(label_text))
        fld_input.click()
        fld_input.send_keys(input_text)

    def input_textarea(self, label_text: str, input_text: str = ""):
        """
        Enter text into the text area with the specified label text

        :param label_text: text of the label specified next to a text area
        :param input_text: text to be entered
        :return:
        """
        fld_input = self.find_element(*TextFieldsLocators.find_textarea_by_label(label_text))
        fld_input.click()
        fld_input.send_keys(input_text)

    def clear_textarea_by_label(self, label_text: str):
        """
        Clear the text area with the specified label text

        :param label_text: text of the label specified next to a text area
        :return:
        """
        fld = self.find_element(*TextFieldsLocators.find_textarea_by_label(label_text))
        fld.click()
        fld.clear()


class TextBoxOutputs(BasePage):

    def get_textbox_output(self) -> dict:
        """
        Get text from a box displaying the resulting text sent into the text field

        :return:
        """
        output_flds = {}
        output = self.find_elements(*TextFieldsLocators.TEXTBOX_OUTPUT)
        time.sleep(2)
        for i in output:
            output_key = i.text.split(':')[0]
            output_value = i.text.split(':')[1]
            output_flds[output_key] = output_value
        try:
            output_flds['Full Name'] = output_flds.pop('Name')
            output_flds['Current Address'] = output_flds.pop('Current Address ')
            output_flds['Permanent Address'] = output_flds.pop('Permananet Address ')
        except KeyError:
            pass
        return output_flds

    def get_incorrectly_filled_fields(self) -> list:
        """
        Get list of incorrectly filled fields

        :return: list of field names (ids)
        """
        fld_err = self.find_elements(*TextFieldsLocators.ERROR_OUTPUT)
        return [i.get_attribute('id') for i in fld_err]


class ClickButtons(BasePage):

    def click_button_by_its_name(self, btn_text: str):
        """
        Locate a button by the text displayed on it and click it

        :param btn_text: text displayed on a button
        :return:
        """
        self.find_element(*ButtonsLocators.find_btn_by_label(btn_text)).click()
        time.sleep(2)


class CheckboxesRadiobuttons(BasePage):

    def find_checkbox_by_label(self, chkbx_lbl: str, click_chkbx: bool = True):
        """
        Find checkbox by the text displayed next to it and click it
        (or not if a relevant argument is set to False)

        :param chkbx_lbl: text displayed next to the checkbox
        :param click_chkbx: True (default) if the found checkbox should be clicked on
                            or False if the click should not be performed
        :return:
        """
        chkbx = self.find_element(*CheckboxesLocators.find_checkbox_by_label(chkbx_lbl))
        try:
            if click_chkbx:
                chkbx.click()
        except ElementClickInterceptedException:
            self.execute_script("arguments[0].scrollIntoView();", chkbx)
            if click_chkbx:
                chkbx.click()

    def open_checkbox_contents(self, chkbx_lbl: str):
        """
        Click on the arrow button next to the checkbox from the Elements - Checkbox page

        :param chkbx_lbl: text displayed next to the checkbox
        :return:
        """
        self.find_element(*CheckboxesLocators.expand_checkbox(chkbx_lbl)).click()
        time.sleep(2)

    def find_radiobtn_by_text(self, radiobtn_text, click_radiobtn: bool = True):
        """
        Find radiobutton by the text displayed next to it and click it
        (or not if a relevant argument is set to False)

        :param radiobtn_text: text displayed next to the radiobutton
        :param click_radiobtn: True (default) if the found radiobutton should be clicked on
                               or False if the click should not be performed
        :return:
        """
        radio = self.find_element(*RadiobuttonsLocators.find_radiobutton_by_text(radiobtn_text))
        if click_radiobtn:
            radio.click()
        time.sleep(2)

    def find_all_checked_checkboxex(self) -> list:
        """
        Find all the selected checkboxes (these are marked with V symbol)

        :return: list of labels displayed next to the selected checkboxes
        """
        checked = self.find_elements(*CheckboxesLocators.get_all_checked())
        return [i.text for i in checked] if len(checked) > 0 else []

    def find_all_halfchecked_checkboxes(self) -> list:
        """
        Find all the 'partially' selected checkboxes (these are marked with - symbol)

        :return: list of labels displayed next to the 'partially' selected checkboxes
        """
        halfchecked = self.find_elements(*CheckboxesLocators.get_all_halfchecked())
        return [i.text for i in halfchecked] if len(halfchecked) > 0 else []

    def check_checkbox_status(self, chkbx_lbl: str) -> str:
        """
        Check the status of a particular checkbox.
        The possible status values are:
        - Checked - if the checkbox is checked (marked with a V symbol)
        - Half Checked - if the checkbox is 'partially' checked (marked with a - symbol)
        - Unchecked - if the checkbox is unchecked (empty)

        :param chkbx_lbl: text displayed next to the checkbox
        :return: checkbox status as text
        """
        if self.find_element(*CheckboxesLocators.is_checkbox_checked(chkbx_lbl)):
            return 'Checked'
        elif self.find_element(*CheckboxesLocators.is_checkbox_halfchecked(chkbx_lbl)):
            return 'Half Checked'
        elif self.find_element(*CheckboxesLocators.is_checkbox_unchecked(chkbx_lbl)):
            return 'Unchecked'
        else:
            return 'Unknown status'

    def expand_all(self):
        """
        Click on the Expand All button (+) from the Elements - Checkbox page

        :return:
        """
        self.find_element(*CheckboxesLocators.CHECKBOX_EXPAND_ALL).click()
        time.sleep(2)

    def verify_radio_inactive(self):
        return self.find_element(*RadiobuttonsLocators.RADIO_INACTIVE).text


class CheckboxesOutputs(BasePage):

    def get_output_for_checked_dir(self) -> list:
        """
        Get the contents of the selected checkboxes displayed below them
        on the Elements - Checkbox page after one or more checkboxes are selected

        :return: list of items (names of directories and/or files) from the result box
        """
        res = self.find_elements(*CheckboxesLocators.CHECKBOX_OUTPUT)
        time.sleep(2)
        return [i.text for i in res]

    def get_output_for_radio(self) -> str:
        """
        Get the result text after a radiobutton was selected

        :return: text displayed next to the radiobutton after its selection
        """
        return self.find_element(*RadiobuttonsLocators.RADIO_RESULT).text


class DropDowns(BasePage):

    def select_state(self, state: str):
        """
        Select a specified state from the drop down list

        :param state: state to be selected
        :return:
        """
        self.find_element(*DropDownLocators.STATE_LOCATOR).send_keys(state, Keys.ENTER)

    def select_city(self, city: str):
        """
        Select a specified city from the drop down list

        :param city: city to be selected
        :return:
        """
        self.find_element(*DropDownLocators.CITY_LOCATOR).send_keys(city, Keys.ENTER)
