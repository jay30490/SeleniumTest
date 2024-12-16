import allure
import pytest

from modules.pages.drag_n_drop import Interactions
from modules.pages.navigation import NavigationMenu
from modules.utils import allure_screenshot_on_failure


@pytest.fixture(autouse = True, scope = 'module')
@allure.title('Go to the Interactions/Resizable page')
def go_to_interactions_resizable_page(browser):
    """
    Fixture for auto-opening the Interactions - Resizable page before tests start.
    This fixture only works once
    """
    NavigationMenu.nav_left_menu(browser, "Interactions", "Resizable")
    yield


@allure.title('14.1 - Check the box default size')
@allure.description('Check the box default size')
@allure.tag('Interactions', "Resizable")
@allure.link(url = 'https://demoqa.com/resizable')
def test_check_default_size(browser, request):
    with allure.step('Verify default box size'):
        exp = ('200px', '200px')
        box_size = Interactions.resize_box_get_size(browser)
        try:
            assert box_size == exp, f'Default box size is incorrect.' \
                                    f'Expected: width = {exp[0]}, height = {exp[1]},' \
                                    f'Actual: width = {box_size[0]}, height = {box_size[1]}'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Default box size is incorrect.' \
                                    f'Expected: width = {exp[0]}, height = {exp[1]},' \
                                    f'Actual: width = {box_size[0]}, height = {box_size[1]}')

box_sizes = [
    (-50, -50, '150px', '150px'),
    (350, 150, '500px', '300px')
]

@pytest.mark.parametrize('x, y, w, h', box_sizes)
@allure.title('14.2 / 14.3 - Change the box size')
@allure.description('Change the box size')
@allure.tag('Interactions', "Resizable")
@allure.link(url = 'https://demoqa.com/resizable')
def test_change_box_size(browser, x, y, w, h, request):
    with allure.step('Change box size'):
        exp = (w, h)
        Interactions.resize_box_change_size(browser, xoffset = x, yoffset = y)
    with allure.step('Verify that the box has correct size'):
        box_size = Interactions.resize_box_get_size(browser)
        try:
            assert box_size == exp, f'Box size is incorrect.' \
                                    f'Expected: width = {w}, height = {h},' \
                                    f'Actual: width = {box_size[0]}, height = {box_size[1]}'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Box size is incorrect.' \
                                    f'Expected: width = {w}, height = {h},' \
                                    f'Actual: width = {box_size[0]}, height = {box_size[1]}'   )