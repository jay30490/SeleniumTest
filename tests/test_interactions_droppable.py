import allure
import pytest

from modules.pages.drag_n_drop import Interactions
from modules.pages.navigation import NavigationMenu
from modules.utils import allure_screenshot_on_failure


@pytest.fixture(autouse = True, scope = 'module')
@allure.title('Go to the Interactions/Droppable page')
def go_to_interactions_droppable_page(browser):
    """
    Fixture for auto-opening the Interactions - Droppable page before tests start.
    This fixture only works once
    """
    NavigationMenu.nav_left_menu(browser, "Interactions", "Droppable")
    yield


@allure.title('15.1 - Drag and drop the box')
@allure.description('Drag the box with the Drag Me text to the Drop Here box '
                    'and verify that the text has changed')
@allure.tag('Interactions', "Droppable")
@allure.link(url = 'https://demoqa.com/droppable')
def test_drop_to_box(browser, request):
    with allure.step('Drag an element to the drop box'):
        exp = 'Dropped!'
        Interactions.droppable_simple(browser)
    with allure.step('Verify that the text has changed to expected after dropping'):
        res = Interactions.get_drop_text(browser)
        try:
            assert res == exp, f'Incorrect text after dropping.' \
                               f'Expected: {exp},' \
                               f'Actual: {res}'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Incorrect text after dropping.' \
                               f'Expected: {exp},' \
                               f'Actual: {res}')
