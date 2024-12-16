import allure
import pytest

from modules.pages.alerts import Alerts
from modules.pages.navigation import NavigationMenu
from modules.utils import allure_screenshot_on_failure


@pytest.fixture(autouse = True, scope = 'module')
@allure.title('Go to the Alerts, Frame & Windows/Alerts page')
def go_to_alerts_page(browser):
    """
    Fixture for auto-opening the Alerts page before tests start.
    This fixture only works once
    """
    NavigationMenu.nav_left_menu(browser, "Alerts, Frame & Windows", "Alerts")
    yield


@allure.title('10.1 - Check the text displayed in Alert')
@allure.description('Check the text displayed in Alert')
@allure.tag('Alerts')
@allure.link(url = 'https://demoqa.com/alerts')
def test_alert_text(browser, request):
    with allure.step('Call simple alert'):
        Alerts.click_alert_btn(browser)
    with allure.step('Get text displayed in alert'):
        alert_txt = Alerts.get_alert_text(browser)
        exp = 'You clicked a button'
    with allure.step('Close alert'):
        Alerts.accept_alert(browser)
    with allure.step('Verify text displayed in alert'):
        try:
            assert alert_txt == exp, f'Incorrect alert text.' \
                                 f'Expected [{exp}],' \
                                 f'Actual [{alert_txt}]'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Incorrect alert text.' \
                                 f'Expected [{exp}],' \
                                 f'Actual [{alert_txt}]')

@allure.title('10.2 - Check the text displayed in a Confirmation Alert')
@allure.description('Check the text displayed in a Confirmation Alert')
@allure.tag('Alerts')
@allure.link(url = 'https://demoqa.com/alerts')
def test_confirm_alert_text(browser, request):
    with allure.step('Call confirmation alert'):
        Alerts.click_confirm_alert_btn(browser)
    with allure.step('Get text displayed in alert'):
        alert_txt = Alerts.get_alert_text(browser)
        exp = 'Do you confirm action?'
    with allure.step('Close alert'):
        Alerts.accept_alert(browser)
    with allure.step('Verify text displayed in alert'):
        try:
            assert alert_txt == exp, f'Incorrect alert text.' \
                                 f'Expected [{exp}],' \
                                 f'Actual [{alert_txt}]'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Incorrect alert text.' \
                                 f'Expected [{exp}],' \
                                 f'Actual [{alert_txt}]')


@allure.title('10.3 - Check the text displayed in a Prompt')
@allure.description('Check the text displayed in a Prompt')
@allure.tag('Alerts')
@allure.link(url = 'https://demoqa.com/alerts')
def test_prompt_alert_text(browser, request):
    with allure.step('Call prompt alert'):
        Alerts.click_prompt_btn(browser)
    with allure.step('Get text displayed in alert'):
        prompt_txt = Alerts.get_alert_text(browser)
        exp = 'Please enter your name'
    with allure.step('Close alert'):
        Alerts.accept_alert(browser)
    with allure.step('Verify text displayed in alert'):
        try:
            assert prompt_txt == exp, f'Incorrect prompt text.' \
                                      f'Expected [{exp}],' \
                                      f'Actual [{prompt_txt}]'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Incorrect prompt text.' \
                                      f'Expected [{exp}],' \
                                      f'Actual [{prompt_txt}]')


@allure.title('10.4 - Accept the Confirmation Alert')
@allure.description('Accept the Confirmation Alert')
@allure.tag('Alerts')
@allure.link(url = 'https://demoqa.com/alerts')
def test_confirm_alert_accept(browser, request):
    with allure.step('Call confirmation alert'):
        Alerts.click_confirm_alert_btn(browser)
    with allure.step('Accept alert'):
        Alerts.accept_alert(browser)
    with allure.step('Verify text displayed on the main screen'):
        actual = Alerts.get_alert_result(browser)
        exp = 'You selected Ok'
        try:
            assert actual == exp, f'Incorrect alert result.' \
                                 f'Expected [{exp}],' \
                                 f'Actual [{actual}]'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Incorrect alert result.' \
                                 f'Expected [{exp}],' \
                                 f'Actual [{actual}]')


@allure.title('10.5 - Dismiss the Confirmation Alert')
@allure.description('Dismiss the Confirmation Alert')
@allure.tag('Alerts')
@allure.link(url = 'https://demoqa.com/alerts')
def test_confirm_alert_dismiss(browser, request):
    with allure.step('Call confirmation alert'):
        Alerts.click_confirm_alert_btn(browser)
    with allure.step('Dismiss alert'):
        Alerts.dismiss_alert(browser)
    with allure.step('Verify text displayed on the main screen'):
        actual = Alerts.get_alert_result(browser)
        exp = 'You selected Cancel'
        try:
            assert actual == exp, f'Incorrect alert result.' \
                                     f'Expected [{exp}],' \
                                     f'Actual [{actual}]'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Incorrect alert result.' \
                                     f'Expected [{exp}],' \
                                     f'Actual [{actual}]')


@allure.title('10.6 - Enter text into the Prompt')
@allure.description('Enter text into the Prompt and check that it is displayed correctly afterwards')
@allure.tag('Alerts')
@allure.link(url = 'https://demoqa.com/alerts')
def test_prompt_alert_enter(browser, request):
    with allure.step('Call prompt alert'):
        enter = 'Hello'
        Alerts.click_prompt_btn(browser)
    with allure.step('Enter text into prompt alert'):
        Alerts.prompt_send_text(browser, input_text = enter)
    with allure.step('Accept alert'):
        Alerts.accept_alert(browser)
    with allure.step('Verify text displayed on the main screen'):
        exp = f'You entered {enter}'
        actual = Alerts.get_prompt_result(browser)
        try:
            assert actual == exp, f'Incorrect prompt result.' \
                                  f'Expected [{exp}],' \
                                  f'Actual [{actual}]'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Incorrect prompt result.' \
                                  f'Expected [{exp}],' \
                                  f'Actual [{actual}]')
