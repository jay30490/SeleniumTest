import allure
import pytest

from modules.pages.drag_n_drop import Interactions
from modules.pages.navigation import NavigationMenu
from modules.utils import allure_screenshot_on_failure


@pytest.fixture(autouse = True, scope = 'module')
@allure.title('Go to the Interactions/Sortable page')
def go_to_interaction_sortable_page(browser):
    """
    Fixture for auto-opening the Interactions - Sortable page before tests start.
    This fixture only works once
    """
    NavigationMenu.nav_left_menu(browser, "Interactions", "Sortable")
    yield


@allure.title('12.1 - Reorder list items')
@allure.description('Reorder list items to the reverse order')
@allure.tag('Interactions', "Sortable")
@allure.link(url = 'https://demoqa.com/sortable')
def test_sort_list(browser, request):
    with allure.step('Change list items order'):
        orig_list = Interactions.sort_list_get_items(browser)
        exp = list(reversed(orig_list))
        for i in orig_list:
            Interactions.sort_list(browser, item1 = i, item2 = orig_list[-1])
    with allure.step('Verify the new list items order'):
        upd_list = Interactions.sort_list_get_items(browser)
        try:
            assert upd_list == exp, f"Updated list is incorrect:" \
                                    f"Expected {exp}," \
                                    f"Actual: {upd_list}"
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f"Updated list is incorrect:" \
                                    f"Expected {exp}," \
                                    f"Actual: {upd_list}")


@allure.title('12.2 - Reorder grid items')
@allure.description('Reorder grid items to the reverse order')
@allure.tag('Interactions', "Sortable")
@allure.link(url = 'https://demoqa.com/sortable')
def test_sort_grid(browser, request):
    with allure.step('Change grid items order'):
        NavigationMenu.tabs_navigation(browser, 'Grid')
        orig_grid = Interactions.sort_grid_get_items(browser)
        exp = list(reversed(orig_grid))
        for i in orig_grid:
            Interactions.sort_grid(browser, item1 = i, item2 = orig_grid[-1])
    with allure.step('Verify the new grid items order'):
        upd_grid = Interactions.sort_grid_get_items(browser)
        try:
            assert upd_grid == exp, f"Updated grid is incorrect:" \
                                    f"Expected {exp}," \
                                    f"Actual: {upd_grid}"
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f"Updated grid is incorrect:" \
                                    f"Expected {exp}," \
                                    f"Actual: {upd_grid}")