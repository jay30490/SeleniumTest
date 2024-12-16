import allure
import pytest

from modules.pages.navigation import NavigationMenu
from modules.pages.web_tables import WebTablesHandling, WebTables
from modules.utils import allure_screenshot_on_failure


@pytest.fixture(autouse = True, scope = 'module')
@allure.title('Go to the Elements/Web Tables page')
def go_to_webtables_page(browser):
    """
    Fixture for auto-opening the Web Tables page before tests start.
    This fixture only works once
    """
    NavigationMenu.nav_left_menu(browser, "Elements", "Web Tables")
    yield


@pytest.fixture(scope = 'function')
@allure.title('Clear the Search field')
def clear_search_fld(browser):
    """
    Fixture for auto-opening the Web Tables page before tests start.
    This fixture only works once
    """
    yield
    WebTablesHandling.clear_search_fld(browser)


headers_abc = ['First Name',
                'Last Name',
                'Email',
                'Department'
               ]

headers_num = ['Age',
               'Salary'
               ]


@pytest.mark.parametrize('sorting', headers_abc)
@allure.title('6.1 - Sorting in ascending order (alphabetical)')
@allure.description('Verify that the entries in the sorted column displayed in the ascending order')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_sorting_abc_asc(browser, sorting, request):
    with allure.step('Sort column in ascending order (alphabetically)'):
        WebTablesHandling.sort_column(browser, sorting)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
        sort_check = [i[sorting] for i in res]
    with allure.step('Verify that the entries in specified column are sorted correctly'):
        try:
            assert all(sort_check[i] <= sort_check[i+1] for i in range(len(sort_check) - 1)), \
                f'Entries in [{sorting}] column are not in expected order'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Entries in [{sorting}] column are not in expected order')


@pytest.mark.parametrize('sorting', headers_abc)
@allure.title('6.2 - Sorting in descending order (alphabetical)')
@allure.description('Verify that the entries in the sorted column displayed in the descending order')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_sorting_abc_desc(browser, sorting, request):
    with allure.step('Sort column in descending order (alphabetically)'):
        WebTablesHandling.sort_column(browser, sorting, dbl_click = True)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
        sort_check = [i[sorting] for i in res]
    with allure.step('Verify that the entries in specified column are sorted correctly'):
        try:
            assert all(sort_check[i] >= sort_check[i + 1] for i in range(len(sort_check) - 1)), \
                f'Entries in [{sorting}] column are not in expected order'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Entries in [{sorting}] column are not in expected order')


@pytest.mark.parametrize('sorting', headers_num)
@allure.title('6.3 - Sorting in ascending order (numerical)')
@allure.description('Verify that the entries in the sorted column displayed in the ascending order')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_sorting_num_asc(browser, sorting, request):
    with allure.step('Sort column in ascending order (numerically)'):
        WebTablesHandling.sort_column(browser, sorting)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
        sort_check = [int(i[sorting]) for i in res]
    with allure.step('Verify that the entries in specified column are sorted correctly'):
        try:
            assert all(sort_check[i] <= sort_check[i + 1] for i in range(len(sort_check) - 1)), \
                f'Entries in [{sorting}] column are not in expected order'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Entries in [{sorting}] column are not in expected order')


@pytest.mark.parametrize('sorting', headers_num)
@allure.title('6.4 - Sorting in descending order (numerical)')
@allure.description('Verify that the entries in the sorted column displayed in the descending order')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_sorting_num_desc(browser, sorting, request):
    with allure.step('Sort column in descending order (numerically)'):
        WebTablesHandling.sort_column(browser, sorting, dbl_click = True)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
        sort_check = [int(i[sorting]) for i in res]
    with allure.step('Verify that the entries in specified column are sorted correctly'):
        try:
            assert all(sort_check[i] >= sort_check[i + 1] for i in range(len(sort_check) - 1)), \
                f'Entries in [{sorting}] column are not in expected order'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Entries in [{sorting}] column are not in expected order')