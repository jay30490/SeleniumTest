import allure
import pytest

from modules.pages.elements import ClickButtons, FieldsInput
from modules.pages.navigation import NavigationMenu
from modules.pages.web_tables import WebTablesEntries, WebTables, WebTablesHandling
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


all_headers = ['First Name',
                'Last Name',
                'Email',
                'Department',
                'Age',
               'Salary',
               ]

email_vals = ['abc@test',
         'abc.com',
         '@test.com',
         ' @test.com',
         'abc@ .com',
         'abc@test.',
         'abc@.com',
         ' ',
              ]

invalid_name = [' ',
                '123',
                '.',
                '?',
                ]

invalid_num_flds = ['a',
                    '1a',
                    '.',
                    '?',
                    ' ',
                    '0',
                    ]

@allure.title('4.1 - Registration Form opening')
@allure.description('Verify that the Registration Form is open upon clicking the Add button')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_check_reg_form_open(browser, request):
    with allure.step('Click "Add" button'):
        ClickButtons.click_button_by_its_name(browser, 'Add')
    with allure.step('Check if the Registration Form window is open'):
        reg_form = WebTablesEntries.check_reg_form_open(browser)
    with allure.step('Close Registration Form window if it is open'):
        WebTablesEntries.close_reg_form(browser)
    with allure.step('Verify that Registration Form window was opened after clicking the "Add" button'):
        try:
            assert reg_form is True, "Registration Form window was not opened"
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError("Registration Form window was not opened")


@allure.title('7.1 - New entry')
@allure.description('Verify that the new entry is added to the table after filling in '
                    'all the fields in the Registration Form with the valid values')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_add_new_entry_valid(browser, request):
    with allure.step('Click "Add" button'):
        ClickButtons.click_button_by_its_name(browser, 'Add')
    with allure.step('Check if the Registration Form window is open'):
        reg_form = WebTablesEntries.check_reg_form_open(browser)
    with allure.step('Add new entry via the Registration Form'):
        reg_data = {
            'First Name': 'John',
            'Last Name': 'Smith',
            'Email': 'johnsmith@test.com',
            'Age': '35',
            'Salary': '15000',
            'Department': 'IT'
        }
        if reg_form:
            for k, v in reg_data.items():
                FieldsInput.input_text(browser, label_text = k, input_text = v)
        with allure.step('Click "Submit" button'):
            ClickButtons.click_button_by_its_name(browser, 'Submit')
        with allure.step('Get table contents'):
            res = WebTables.get_tbl_contents(browser)
        with allure.step('Verify that new entry appeared correctly in the table'):
            try:
                assert reg_data in res, 'Row not found'
            except AssertionError:
                allure_screenshot_on_failure(browser, request)
                raise AssertionError('Row not found')


@allure.title('7.2 - Duplicate entry')
@allure.description('Verify that the duplicate entry is not added to the table')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_add_duplicate_entry(browser, request):
    with allure.step('Click "Add" button'):
        ClickButtons.click_button_by_its_name(browser, 'Add')
    with allure.step('Check if the Registration Form window is open'):
        reg_form = WebTablesEntries.check_reg_form_open(browser)
    with allure.step('Add new entry via the Registration Form'):
        reg_data = {
            'First Name': 'Jane',
            'Last Name': 'Smith',
            'Email': 'janesmith@test.com',
            'Age': '30',
            'Salary': '16000',
            'Department': 'IT'
        }
        if reg_form:
            for k, v in reg_data.items():
                FieldsInput.input_text(browser, label_text = k, input_text = v)
    with allure.step('Click "Submit" button'):
        ClickButtons.click_button_by_its_name(browser, 'Submit')
    with allure.step('Click "Add" button'):
        ClickButtons.click_button_by_its_name(browser, 'Add')
    with allure.step('Check if the Registration Form window is open'):
        reg_form = WebTablesEntries.check_reg_form_open(browser)
    with allure.step('Add the same entry via the Registration Form'):
        if reg_form:
            for k, v in reg_data.items():
                FieldsInput.input_text(browser, label_text = k, input_text = v)
    with allure.step('Click "Submit" button'):
        ClickButtons.click_button_by_its_name(browser, 'Submit')
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Verify that the duplicated entry was not added'):
        try:
            assert reg_data not in res, 'Entry unexpectedly added'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError('Entry unexpectedly added')


@pytest.mark.parametrize('flds', all_headers)
@allure.title('7.3 - Empty field')
@allure.description('Verify that the entry without a value in a single field is not added to the table')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_leave_one_field_empty(browser, flds, request):
    with allure.step('Click "Add" button'):
        ClickButtons.click_button_by_its_name(browser, 'Add')
    with allure.step('Check if the Registration Form window is open'):
        reg_form = WebTablesEntries.check_reg_form_open(browser)
    with allure.step('Add new entry via the Registration Form but leave one field empty'):
        reg_data = {
            'First Name': 'Jack',
            'Last Name': 'Smith',
            'Email': 'jacksmith@test.com',
            'Age': '25',
            'Salary': '12000',
            'Department': 'IT'
        }
        if reg_form:
            for fld in all_headers:
                FieldsInput.clear_textfield_by_label(browser, label_text = fld)
            for k, v in reg_data.items():
                if k != flds:
                    FieldsInput.input_text(browser, label_text = k, input_text = v)
    with allure.step('Click "Submit" button'):
        ClickButtons.click_button_by_its_name(browser, 'Submit')
    with allure.step('Check if the Registration Form window is open and close it if it is'):
        regformopen = WebTablesEntries.check_reg_form_open(browser)
        if regformopen:
            WebTablesEntries.close_reg_form(browser)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Verify that entry was not added'):
        try:
            assert reg_data not in res, 'Entry without required field added'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError('Entry without required field added')


@pytest.mark.parametrize('email', email_vals)
@allure.title('7.4 - Email field vaidation')
@allure.description('Verify that the entry with Email value not following the aaa@bbb.ccc format'
              ' is not added to the table')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_invalid_email(browser, email, request):
    with allure.step('Click "Add" button'):
        ClickButtons.click_button_by_its_name(browser, 'Add')
    with allure.step('Check if the Registration Form window is open'):
        reg_form = WebTablesEntries.check_reg_form_open(browser)
    with allure.step('Add new entry via the Registration Form having Email in an incorrect format'):
        reg_data = {
            'First Name': 'Jack',
            'Last Name': 'Smith',
            'Email': email,
            'Age': '25',
            'Salary': '12000',
            'Department': 'IT'
        }
        if reg_form:
            for fld in all_headers:
                FieldsInput.clear_textfield_by_label(browser, label_text = fld)
            for k, v in reg_data.items():
                FieldsInput.input_text(browser, label_text = k, input_text = v)
    with allure.step('Click "Submit" button'):
        ClickButtons.click_button_by_its_name(browser, 'Submit')
    with allure.step('Check if the Registration Form window is open and close it if it is'):
        regformopen = WebTablesEntries.check_reg_form_open(browser)
        if regformopen:
            WebTablesEntries.close_reg_form(browser)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Verify that entry was not added'):
        try:
            assert reg_data not in res, f'Entry with invalid email format [{email}] added'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Entry with invalid email format [{email}] added')


@pytest.mark.parametrize('name', invalid_name)
@allure.title('7.5 - First Name field validation')
@allure.description('Verify that the entry with symbols other than letters and - for the First Name value'
              ' is not added to the table')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_invalid_first_name(browser, name, request):
    with allure.step('Click "Add" button'):
        ClickButtons.click_button_by_its_name(browser, 'Add')
    with allure.step('Check if the Registration Form window is open'):
        reg_form = WebTablesEntries.check_reg_form_open(browser)
    with allure.step('Add new entry via the Registration Form having First Name in an incorrect format'):
        reg_data = {
            'First Name': name,
            'Last Name': 'Smith',
            'Email': 'jacksmith@test.com',
            'Age': '25',
            'Salary': '12000',
            'Department': 'IT'
        }
        if reg_form:
            for fld in all_headers:
                FieldsInput.clear_textfield_by_label(browser, label_text = fld)
            for k, v in reg_data.items():
                FieldsInput.input_text(browser, label_text = k, input_text = v)
    with allure.step('Click "Submit" button'):
        ClickButtons.click_button_by_its_name(browser, 'Submit')
    with allure.step('Check if the Registration Form window is open and close it if it is'):
        regformopen = WebTablesEntries.check_reg_form_open(browser)
        if regformopen:
            WebTablesEntries.close_reg_form(browser)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Verify that entry was not added'):
        try:
            assert reg_data not in res, f'Entry with invalid symbol [{name}] in First Name added'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Entry with invalid symbol [{name}] in First Name added')


@pytest.mark.parametrize('name', invalid_name)
@allure.title('7.6 - Last Name field validation')
@allure.description('Verify that the entry with symbols other than letters and - for the Last Name value'
              ' is not added to the table')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_invalid_last_name(browser, name, request):
    with allure.step('Click "Add" button'):
        ClickButtons.click_button_by_its_name(browser, 'Add')
    with allure.step('Check if the Registration Form window is open'):
        reg_form = WebTablesEntries.check_reg_form_open(browser)
    with allure.step('Add new entry via the Registration Form having Last Name in an incorrect format'):
        reg_data = {
            'First Name': 'Jack',
            'Last Name': name,
            'Email': 'jacksmith@test.com',
            'Age': '25',
            'Salary': '12000',
            'Department': 'IT'
        }
        if reg_form:
            for fld in all_headers:
                FieldsInput.clear_textfield_by_label(browser, label_text = fld)
            for k, v in reg_data.items():
                FieldsInput.input_text(browser, label_text = k, input_text = v)
    with allure.step('Click "Submit" button'):
        ClickButtons.click_button_by_its_name(browser, 'Submit')
    with allure.step('Check if the Registration Form window is open and close it if it is'):
        regformopen = WebTablesEntries.check_reg_form_open(browser)
        if regformopen:
            WebTablesEntries.close_reg_form(browser)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Verify that entry was not added'):
        try:
            assert reg_data not in res, f'Entry with invalid symbol [{name}] in Last Name added'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Entry with invalid symbol [{name}] in Last Name added')


@pytest.mark.parametrize('age', invalid_num_flds)
@allure.title('7.7 / 7.9 - Age field validation')
@allure.description('Verify that the entry with symbols other than numbers > 0 for the Age field value'
              ' is not added to the table')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_invalid_age(browser, age, request):
    with allure.step('Click "Add" button'):
        ClickButtons.click_button_by_its_name(browser, 'Add')
    with allure.step('Check if the Registration Form window is open'):
        reg_form = WebTablesEntries.check_reg_form_open(browser)
    with allure.step('Add new entry via the Registration Form having Age in an incorrect format'):
        reg_data = {
            'First Name': 'Jack',
            'Last Name': 'Smith',
            'Email': 'jacksmith@test.com',
            'Age': age,
            'Salary': '12000',
            'Department': 'IT'
        }
        if reg_form:
            for fld in all_headers:
                FieldsInput.clear_textfield_by_label(browser, label_text = fld)
            for k, v in reg_data.items():
                FieldsInput.input_text(browser, label_text = k, input_text = v)
    with allure.step('Click "Submit" button'):
        ClickButtons.click_button_by_its_name(browser, 'Submit')
    with allure.step('Check if the Registration Form window is open and close it if it is'):
        regformopen = WebTablesEntries.check_reg_form_open(browser)
        if regformopen:
            WebTablesEntries.close_reg_form(browser)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Verify that entry was not added'):
        try:
            assert reg_data not in res, f'Entry with [{age}] in Age field added'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Entry with [{age}] in Age field added')


@pytest.mark.parametrize('salary', invalid_num_flds)
@allure.title('7.8 / 7.10 - Salary field validation')
@allure.description('Verify that the entry with symbols other than numbers > 0 for the Salary field value'
              ' is not added to the table')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_invalid_salary(browser, salary, request):
    with allure.step('Click "Add" button'):
        ClickButtons.click_button_by_its_name(browser, 'Add')
    with allure.step('Check if the Registration Form window is open'):
        reg_form = WebTablesEntries.check_reg_form_open(browser)
    with allure.step('Add new entry via the Registration Form having Salary in an incorrect format'):
        reg_data = {
            'First Name': 'Jack',
            'Last Name': 'Smith',
            'Email': 'jacksmith@test.com',
            'Age': '25',
            'Salary': salary,
            'Department': 'IT'
        }
        if reg_form:
            for fld in all_headers:
                FieldsInput.clear_textfield_by_label(browser, label_text = fld)
            for k, v in reg_data.items():
                FieldsInput.input_text(browser, label_text = k, input_text = v)
    with allure.step('Click "Submit" button'):
        ClickButtons.click_button_by_its_name(browser, 'Submit')
    with allure.step('Check if the Registration Form window is open and close it if it is'):
        regformopen = WebTablesEntries.check_reg_form_open(browser)
        if regformopen:
            WebTablesEntries.close_reg_form(browser)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Verify that entry was not added'):
        try:
            assert reg_data not in res, f'Entry with [{salary}] in Salary field added'
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f'Entry with [{salary}] in Salary field added')