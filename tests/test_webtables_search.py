import allure
import pytest

from modules.pages.navigation import NavigationMenu
from modules.pages.web_tables import WebTables, WebTablesHandling
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


search_for_exist = ['in', 'try', '2000', '10000', '@']

search_for_nonexist = ['aaa', '9999', '!', '>', '?', '.' ' ']

row_count_values = [5, 25, 100]


@pytest.mark.parametrize('rows', row_count_values)
@allure.title('4.2 - Row count')
@allure.description('Verify that the displayed rows count is as value selected from the drop down list')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_row_count(browser, rows, request):
    with allure.step('Change row count'):
        WebTablesHandling.change_row_count(browser, row_count = f'{rows} rows')
    with allure.step('Verify that new row count is as expected'):
        res = WebTables.get_rows_num(browser)
        try:
            assert res == rows, f'Expected row count [{rows}]. Actual row count [{res}]'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Expected row count [{rows}]. Actual row count [{res}]')


@allure.title('4.3 - Verify entry exists (by all fields)')
@allure.description('Verify that the entry with the specified field values exists in the table')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_full_row_search_valid(browser, request):
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Search for a row by full match'):
        search_for = {'First Name': 'Alden',
                     'Last Name': 'Cantrell',
                     'Age': '45',
                     'Email': 'alden@example.com',
                     'Salary': '12000',
                     'Department': 'Compliance'
                     }
    with allure.step('Verify that the row in search exists in the table'):
        try:
            assert search_for in res, 'Row not found'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError('Row not found')


@allure.title('4.4 - Verify entry does not exist (by all fields)')
@allure.description('Verify that the entry with the specified field values does not exist in the table')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_full_row_search_negative(browser, request):
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Search for a non-existing row by full match'):
        search_for = {'First Name': 'Alden',
                     'Last Name': 'Cantrell',
                     'Age': '47',
                     'Email': 'alden@example.com',
                     'Salary': '12000',
                     'Department': 'Compliance'
                     }
    with allure.step('Verify that the row in search does not exist in the table'):
        try:
            assert search_for not in res, 'Unexpected row found'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError('Unexpected row found')


@pytest.mark.parametrize('search', search_for_exist)
@allure.title('5.1 / 5.3 - Search field - existing entry')
@allure.description('Enter several symbols contained in one or several entries into the Search field')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_search_field_existing(browser, search, clear_search_fld, request):
    with allure.step('Enter data in Search field'):
        WebTablesHandling.search_field(browser, search)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
        for i in res:
            vals = ' '.join(list(i.values())).lower()
    with allure.step('Verify that all displayed entries have rows matching the search data'):
        try:
            assert search in vals, 'No matching rows found'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError('No matching rows found')


@pytest.mark.parametrize('search', search_for_nonexist)
@allure.title('5.2 / 5.4 - Search field - non existing entry')
@allure.description('Enter several symbols not contained in any of the entries into the Search field')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_search_field_nonexisting(browser, search, clear_search_fld, request):
    with allure.step('Enter data in Search field'):
        WebTablesHandling.search_field(browser, search)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
        for i in res:
            vals = ' '.join(list(i.values())).lower()
    with allure.step('Verify that there are no entries displayed'):
        try:
            assert search not in vals, 'Unexpected matching rows found'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError('Unexpected matching rows found')