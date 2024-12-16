import allure
import pytest

from modules.pages.elements import CheckboxesRadiobuttons
from modules.pages.elements import CheckboxesOutputs
from modules.pages.navigation import NavigationMenu
from modules.utils import allure_screenshot_on_failure


@pytest.fixture(autouse = True, scope = 'module')
@allure.title('Go to the AElements/Radio Button page')
def go_to_radiobuttons_page(browser):
    """
    Fixture for auto-opening the Radio Button page before tests start.
    This fixture only works once
    """
    NavigationMenu.nav_left_menu(browser, "Elements", "Radio Button")
    yield


radios = ['Yes', 'Impressive']

@pytest.mark.parametrize('btns', radios)
@allure.title('3.1 - Check the text displayed next to the radiobutton')
@allure.description('Check the text displayed next to the radiobutton after its selection')
@allure.tag('Elements', 'Radiobuttons')
@allure.link(url = 'https://demoqa.com/radio-button')
def test_select_radio(browser, btns, request):
    with allure.step('Select radiobutton'):
        CheckboxesRadiobuttons.find_radiobtn_by_text(browser, btns)
    with allure.step('Verify text after radiobutton selection'):
        actual = CheckboxesOutputs.get_output_for_radio(browser)
        try:
            assert btns == actual, f'Expected text: "You have selected [{btns}]", ' \
                                   f'Actual text: You have selected [{actual}]'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Expected text: "You have selected [{btns}]", ' \
                                   f'Actual text: You have selected [{actual}]')


@allure.title('3.2 - Verify that the radiobutton is inactive')
@allure.description('Verify that the radiobutton is inactive')
@allure.tag('Elements', 'Radiobuttons')
@allure.link(url = 'https://demoqa.com/radio-button')
def test_inactive_radiobtn(browser, request):
    with allure.step('Verify that radiobutton is disabled'):
        CheckboxesRadiobuttons.find_radiobtn_by_text(browser, 'No', click_radiobtn = False)
        actual = CheckboxesRadiobuttons.verify_radio_inactive(browser)
        try:
            assert actual == 'No', 'Radiobutton with label "No" should be disabled'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError('Radiobutton with label "No" should be disabled')