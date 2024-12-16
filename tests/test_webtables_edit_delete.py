import allure
import pytest

from modules.pages.elements import ClickButtons
from modules.pages.elements import FieldsInput
from modules.pages.navigation import NavigationMenu
from modules.pages.web_tables import WebTables
from modules.pages.web_tables import WebTablesEntries
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


reg_data_new_entry = {
        'First Name': 'Jack',
        'Last Name': 'Smith',
        'Email': 'jacksmith@test.com',
        'Age': '25',
        'Salary': '12000',
        'Department': 'IT'
    }

@pytest.fixture(scope = 'function')
@allure.title('Add new entry to the table')
def add_new_entry(browser):
    res = WebTables.get_tbl_contents(browser)
    if reg_data_new_entry not in res:
        ClickButtons.click_button_by_its_name(browser, 'Add')
        reg_form = WebTablesEntries.check_reg_form_open(browser)
        if reg_form:
            for fld in all_headers:
                FieldsInput.clear_textfield_by_label(browser, label_text = fld)
            for k, v in reg_data_new_entry.items():
                FieldsInput.input_text(browser, label_text = k, input_text = v)
            ClickButtons.click_button_by_its_name(browser, 'Submit')
    else:
        print('Already presented')
    yield


all_headers = ['First Name',
                'Last Name',
                'Email',
                'Department',
                'Age',
               'Salary',
               ]

headers_validation = ['Age,'
                      'Salary',
                      'Email',
                      ]

reg_data_edit = {
        'First Name': 'John',
        'Last Name': 'Doe',
        'Email': 'johndoe@test.com',
        'Age': '30',
        'Salary': '8000',
        'Department': 'Accounting'
    }

invalid_num_flds = ['a',
                    '1a',
                    '.',
                    '?',
                    ' ',
                    '0',
                    ]

invalid_email = ['abc@test',
                 'abc.com',
                 '@test.com',
                 ' @test.com',
                 'abc@ .com',
                 'abc@test.',
                 'abc@.com',
                 ' ',
                      ]


@pytest.mark.parametrize('edit', all_headers)
@allure.title('8.1 - Edit a single field value in existing entry')
@allure.description('Edit a single field value in existing entry')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_edit_entry_single_fld(browser, add_new_entry, edit, request):
    with allure.step('Edit single field in entry'):
        WebTablesEntries.edit_delete_entry(browser, first_name = reg_data_new_entry['First Name'],
                                           last_name = reg_data_new_entry['Last Name'],
                                           age = reg_data_new_entry['Age'],
                                           email = reg_data_new_entry['Email'],
                                           salary = reg_data_new_entry['Salary'],
                                           department = reg_data_new_entry['Department'],
                                           action = 'Edit')
    with allure.step('Check if the Refistration Form window is open and enter new data if it is'):
        regformopen = WebTablesEntries.check_reg_form_open(browser)
        if regformopen:
            FieldsInput.clear_textfield_by_label(browser, edit)
            FieldsInput.input_text(browser, label_text = edit,
                                   input_text = reg_data_edit[edit])
            ClickButtons.click_button_by_its_name(browser, 'Submit')
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Verify that edited entry appeared correctly in the table'):
        # making a copy of the reg_data_new_entry dict to avoid changing the values in new entries
        new_data = reg_data_new_entry.copy()
        new_data[edit] = reg_data_edit[edit]
        try:
            assert new_data in res and reg_data_new_entry not in res, "Entry was not updated"
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError("Entry was not updated")


@allure.title('8.2 - Edit all field values in existing entry')
@allure.description('Edit all field values in existing entry')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_edit_entry_all_flds(browser, add_new_entry, request):
    with allure.step('Edit all fields in entry'):
        WebTablesEntries.edit_delete_entry(browser, first_name = reg_data_new_entry['First Name'],
                                           last_name = reg_data_new_entry['Last Name'],
                                           age = reg_data_new_entry['Age'],
                                           email = reg_data_new_entry['Email'],
                                           salary = reg_data_new_entry['Salary'],
                                           department = reg_data_new_entry['Department'],
                                           action = 'Edit')
    with allure.step('Check if the Refistration Form window is open and enter new data if it is'):
        regformopen = WebTablesEntries.check_reg_form_open(browser)
        if regformopen:
            for k, v in reg_data_edit.items():
                FieldsInput.clear_textfield_by_label(browser, k)
                FieldsInput.input_text(browser, label_text = k,
                                       input_text = v)
            ClickButtons.click_button_by_its_name(browser, 'Submit')
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Verify that edited entry appeared correctly in the table'):
        try:
            assert reg_data_edit in res and reg_data_new_entry not in res, "Entry was not updated"
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError("Entry was not updated")


@pytest.mark.parametrize('edit', invalid_email)
@allure.title('8.3 - Edit Email field value (negative test)')
@allure.description('Verify that Email value in existing entry cannot be changed to value '
              'in format other than aaa@bbb.ccc')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_edit_entry_email_invalid(browser, edit, add_new_entry, request):
    fld = 'Email'
    with allure.step('Edit email to incorrect format'):
        WebTablesEntries.edit_delete_entry(browser, first_name = reg_data_new_entry['First Name'],
                                           last_name = reg_data_new_entry['Last Name'],
                                           age = reg_data_new_entry['Age'],
                                           email = reg_data_new_entry['Email'],
                                           salary = reg_data_new_entry['Salary'],
                                           department = reg_data_new_entry['Department'],
                                           action = 'Edit')
    with allure.step('Check if the Refistration Form window is open and enter new data if it is'):
        regformopen = WebTablesEntries.check_reg_form_open(browser)
        if regformopen:
            FieldsInput.clear_textfield_by_label(browser, fld)
            FieldsInput.input_text(browser, label_text = fld,
                                   input_text = edit)
            ClickButtons.click_button_by_its_name(browser, 'Submit')
    with allure.step('Check if the Refistration Form window is still open and close it'):
        regformopen = WebTablesEntries.check_reg_form_open(browser)
        if regformopen:
            WebTablesEntries.close_reg_form(browser)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Verify that edited entry did not appear in the table'):
        # making a copy of the reg_data_new_entry dict to avoid changing the values in new entries
        new_data = reg_data_new_entry.copy()
        new_data[fld] = edit
        try:
            assert new_data not in res and reg_data_new_entry in res, "Entry was unexpectedly updated"
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError("Entry was unexpectedly updated")


num_flds = ['Age', 'Salary']
@pytest.mark.parametrize('edit', invalid_num_flds)
@pytest.mark.parametrize('fld', num_flds)
@allure.title('8.3 - Edit Age and Salary fields values (negative test)')
@allure.description('Verify that Age and Salary values in existing entry '
                    'cannot be changed to non numerical values')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_edit_entry_age_salary_invalid(browser, fld, edit, add_new_entry, request):
    with allure.step('Edit numeric fields in entry'):
        WebTablesEntries.edit_delete_entry(browser, first_name = reg_data_new_entry['First Name'],
                                           last_name = reg_data_new_entry['Last Name'],
                                           age = reg_data_new_entry['Age'],
                                           email = reg_data_new_entry['Email'],
                                           salary = reg_data_new_entry['Salary'],
                                           department = reg_data_new_entry['Department'],
                                           action = 'Edit')
    with allure.step('Check if the Refistration Form window is open and enter new data if it is'):
        regformopen = WebTablesEntries.check_reg_form_open(browser)
        if regformopen:
            FieldsInput.clear_textfield_by_label(browser, fld)
            FieldsInput.input_text(browser, label_text = fld,
                                   input_text = edit)
            ClickButtons.click_button_by_its_name(browser, 'Submit')
    with allure.step('Check if the Refistration Form window is still open and close it'):
        regformopen = WebTablesEntries.check_reg_form_open(browser)
        if regformopen:
            WebTablesEntries.close_reg_form(browser)
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Verify that edited entry did not appear in the table'):
        # making a copy of the reg_data_new_entry dict to avoid changing the values in new entries
        new_data = reg_data_new_entry.copy()
        new_data[fld] = edit
        try:
            assert new_data not in res and reg_data_new_entry in res, "Entry was unexpectedly updated"
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError("Entry was unexpectedly updated")


@allure.title('9.1 - Delete existing entry')
@allure.description('Delete existing entry')
@allure.tag('Elements', "Web Tables")
@allure.link(url = 'https://demoqa.com/webtables')
def test_delete_entry(browser, add_new_entry, request):
    with allure.step('Delete entry by full match'):
        WebTablesEntries.edit_delete_entry(browser, first_name = reg_data_new_entry['First Name'],
                                           last_name = reg_data_new_entry['Last Name'],
                                           age = reg_data_new_entry['Age'],
                                           email = reg_data_new_entry['Email'],
                                           salary = reg_data_new_entry['Salary'],
                                           department = reg_data_new_entry['Department'],
                                           action = 'Delete')
    with allure.step('Get table contents'):
        res = WebTables.get_tbl_contents(browser)
    with allure.step('Verify that the entry is deleted'):
        try:
            assert reg_data_new_entry not in res, "Entry was not deleted"
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError("Entry was not deleted")