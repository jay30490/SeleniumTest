import allure
import pytest

from modules.pages.elements import FieldsInput
from modules.pages.elements import ClickButtons
from modules.pages.elements import TextBoxOutputs
from modules.pages.navigation import NavigationMenu
from modules.utils import allure_screenshot_on_failure


@pytest.fixture(autouse = True, scope = 'module')
@allure.title('Go to the Elements/Text Box page')
def go_to_textbox_page(browser):
    """
    Fixture for auto-opening the Text Box page before tests start.
    This fixture only works once
    """
    NavigationMenu.nav_left_menu(browser, "Elements", "Text Box")
    yield


@pytest.fixture
@allure.title('Clear all the fields after the test')
def clear_fields(browser):
    """
    Fixture for clearing all the fields after the test.
    If you need to clear a particular field/s, specify this explicitly inside the test
    """
    yield
    FieldsInput.clear_textfield_by_label(browser, 'Full Name')
    FieldsInput.clear_textfield_by_label(browser, 'Email')
    FieldsInput.clear_textarea_by_label(browser, 'Current Address')
    FieldsInput.clear_textarea_by_label(browser, 'Permanent Address')


@allure.title('1.1 - Validate that the output result is the same as the input data')
@allure.description('Validate that the output result is the same as the input data')
@allure.tag('Elements', 'Textbox')
@allure.link(url = 'https://demoqa.com/text-box')
def test_text_box_valid_result_validation(browser, clear_fields, request):
    """
    Validate that the output result is the same as the input data

    :param browser: webdriver
    :param clear_fields: fixture call
    :return: none
    """
    with allure.step('Input valid values into fields'):
        input_values_valid = {"Full Name": "Test",
                              "Email": "abc@test.com",
                              "Current Address": "My address",
                              "Permanent Address": "My another address",
                              }

        FieldsInput.input_text(browser, "Full Name", input_values_valid['Full Name'])
        FieldsInput.input_text(browser, "Email", input_values_valid['Email'])
        FieldsInput.input_textarea(browser, "Current Address", input_values_valid['Current Address'])
        FieldsInput.input_textarea(browser, "Permanent Address", input_values_valid['Permanent Address'])
    with allure.step('Click "Submit" button'):
        ClickButtons.click_button_by_its_name(browser, "Submit")
    with allure.step('Verify output'):
        res = TextBoxOutputs.get_textbox_output(browser)
        try:
            assert res == input_values_valid, "Output values don't match the input"
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError("Output values don't match the input")


email_values = [('abc'),
                ('abc@test'),
                ('@test.com'),
                (' @test.com'),
                ('abc.com'),
                (' ')
                ]


@pytest.mark.parametrize('email_val', email_values)
@allure.title('1.2 - Verify that the Email field takes only the data in aaa@bbb.ccc format')
@allure.description('Verify that the Email field takes only the data in aaa@bbb.ccc format')
@allure.tag('Elements', 'Textbox')
@allure.link(url = 'https://demoqa.com/text-box')
def test_text_box_email_validations(browser, email_val, request):
    """
    This is a negative test. It takes one value from the email_values list for each itertation.
    Validate that the Email field only takes values in aaa@bbb.ccc format

    :param browser: webdriver
    :param email_val: values for the Email field
    :return:
    """
    with allure.step('Input email in invalid format'):
        FieldsInput.clear_textfield_by_label(browser, 'Email')
        FieldsInput.input_text(browser, "Email", email_val)
    with allure.step('Click "Submit" button'):
        ClickButtons.click_button_by_its_name(browser, "Submit")
    with allure.step('Verify that "Email" field has an error'):
        res = TextBoxOutputs.get_incorrectly_filled_fields(browser)
        try:
            assert ''.join(res) == 'userEmail', f'The value ({email_val}) did not trigger an error'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'The value ({email_val}) did not trigger an error')
