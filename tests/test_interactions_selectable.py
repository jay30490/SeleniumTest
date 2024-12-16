import allure
import pytest

from modules.pages.drag_n_drop import Interactions
from modules.pages.navigation import NavigationMenu
from modules.utils import allure_screenshot_on_failure


@pytest.fixture(autouse = True, scope = 'module')
@allure.title('Go to the Interactions/Selectable page')
def go_to_interaction_selectable_page(browser):
    """
    Fixture for auto-opening the Interactions - Selectable page before tests start.
    This fixture only works once
    """
    NavigationMenu.nav_left_menu(browser, "Interactions", "Selectable")
    yield


@allure.title('13.1 - Select list elements by text')
@allure.description('Select list elements by text')
@allure.tag('Interactions', "Selectable")
@allure.link(url = 'https://demoqa.com/selectable')
def test_select_list_by_text(browser, request):
    with allure.step('Select list items by exact text match'):
        select_item = ['Morbi leo risus', 'Cras justo odio']
        Interactions.select_list_exact_text(browser, 'Morbi leo risus', 'Cras justo odio')
    with allure.step('Verify that selected items are as expected'):
        res = Interactions.get_selected_list_items(browser)
        try:
            assert res.sort() == select_item.sort(), f'Selected items are incorrect.' \
                                                     f'Expected: {select_item},' \
                                                     f'Actual: {res}'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Selected items are incorrect.'\
                                 f'Expected: {select_item},'\
                                 f'Actual: {res}')


@allure.title('13.2 - Select grid elements by text')
@allure.description('Select grid elements by text')
@allure.tag('Interactions', "Selectable")
@allure.link(url = 'https://demoqa.com/selectable')
def test_select_grid_by_text(browser, request):
    with allure.step('Select grid items by exact text match'):
        NavigationMenu.tabs_navigation(browser, 'Grid')
        select_item = ['One', 'Three', 'Six']
        Interactions.select_grid_exact_text(browser, 'One', 'Three', 'Six')
    with allure.step('Verify that selected items are as expected'):
        res = Interactions.get_selected_grid_items(browser)
        try:
            assert res.sort() == select_item.sort(), f'Selected items are incorrect.' \
                                                     f'Expected: {select_item},' \
                                                     f'Actual: {res}'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Selected items are incorrect.' \
                                 f'Expected: {select_item},' \
                                 f'Actual: {res}')
