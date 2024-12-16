import allure
import pytest

from modules.pages.widgets import Slider
from modules.pages.navigation import NavigationMenu
from modules.utils import allure_screenshot_on_failure


@pytest.fixture(autouse = True, scope = 'module')
@allure.title('Go to the Widgets/Slider page')
def go_to_slider_page(browser):
    """
    Fixture for auto-opening the Widgets - Slider page before tests start.
    This fixture only works once
    """
    NavigationMenu.nav_left_menu(browser, "Widgets", "Slider")
    yield


@allure.title('11.1 - Check the default slider value')
@allure.description('Check the default slider value')
@allure.tag('Widgets', "Slider")
@allure.link(url = 'https://demoqa.com/slider')
def test_check_default_value(browser, request):
    default_value = '25'
    with allure.step('Get current value'):
        def_val = Slider.get_current_value(browser)
    with allure.step('Verify that default value is as expected'):
        try:
            assert def_val == default_value, f'Expected default value: {default_value},' \
                                             f'Actual default value: {def_val}'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Expected default value: {default_value},' \
                                             f'Actual default value: {def_val}')


@allure.title('11.2 - Check the minimum slider value')
@allure.description('Check the minimum slider value')
@allure.tag('Widgets', "Slider")
@allure.link(url = 'https://demoqa.com/slider')
def test_check_min_value(browser, request):
    with allure.step('Get minimum value'):
        min_val = Slider.get_slider_min(browser)
    with allure.step('Vefify that minimum value is 0'):
        try:
            assert min_val == '0', f'Expected minimum value: 0' \
                                   f'Actual minimum value: {min_val}'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Expected minimum value: 0' \
                                   f'Actual minimum value: {min_val}')


@allure.title('11.3 - Check the maximum slider value')
@allure.description('Check the maximum slider value')
@allure.tag('Widgets', "Slider")
@allure.link(url = 'https://demoqa.com/slider')
def test_check_max_value(browser, request):
    with allure.step('Get maximum value'):
        max_val = Slider.get_slider_max(browser)
    with allure.step('Vefify that maximum value is 100'):
        try:
            assert max_val == '100', f'Expected maximum value: 0' \
                                     f'Actual maximum value: {max_val}'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Expected maximum value: 0' \
                                 f'Actual maximum value: {max_val}')


slider_val = [1, 25, 50, 75, 99]


@pytest.mark.parametrize('val', slider_val)
@allure.title('11.4 - Change slider value')
@allure.description('Change slider value')
@allure.tag('Widgets', "Slider")
@allure.link(url = 'https://demoqa.com/slider')
def test_set_slider_value(browser, val, request):
    """
    Min Value = 0
    Max Value = 100
    The value 50 is equal to offset = 1
    The value 0 is equal to offset = -245
    The value 100 is equal to offset 245
    For the values in range [0-50) the provided offset should be negative int with the step = 5,
    where offset = -245 means 0, offset = -240 means 1, etc
    For the values in range (51-100] the provided offset should be positive int with the step = 5,
    where offset = 5 means 51, offset = 10 means 52 etc
    :param browser:
    :return:
    """
    min_offset = -246
    max_offset = 248
    slider_step = 5

    if val in range(1, 50):
        new_offset = int(1 - slider_step * (50 - val))
        Slider.set_slider_value(browser, new_value = new_offset)
        cur_value = Slider.get_current_value(browser)
        print('\nOffset:', new_offset, ' - ', 'Value:', cur_value)
    elif val in range(50, 100):
        new_offset = int(0 + slider_step * (abs(50 - val)))
        Slider.set_slider_value(browser, new_value = new_offset)
        cur_value = Slider.get_current_value(browser)
        print('\nOffset:', new_offset, ' - ', 'Value:', cur_value)
    elif val == 0:
        new_offset = min_offset
    elif val == 100:
        new_offset = max_offset
    else:
        new_offset = 1

    print('OFFSET: ', new_offset)
    with allure.step('Change slider value'):
        Slider.set_slider_value(browser, new_value = new_offset)
    with allure.step('Get current value'):
        cur_val = int(Slider.get_current_value(browser))
    with allure.step(f'Verify that current value is {val}'):
        try:
            assert cur_val == val, f'Incorrect slider value.' \
                                   f'Expected value - [{val}]' \
                                   f'Actual value - [{cur_val}]'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Incorrect slider value.' \
                                   f'Expected value - [{val}]' \
                                   f'Actual value - [{cur_val}]')


