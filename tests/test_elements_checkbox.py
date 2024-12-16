import allure
import pytest
import time

from modules.pages.elements import CheckboxesRadiobuttons
from modules.pages.elements import CheckboxesOutputs
from modules.pages.navigation import NavigationMenu
from modules.utils import allure_screenshot_on_failure


@pytest.fixture(autouse = True, scope = 'module')
@allure.title('Go to the Elements/Check Box page')
def go_to_checkbox_page(browser):
    """
    Fixture for auto-opening the Check Box page before tests start
    and clicking on the Expand All button.
    This fixture only works once
    """
    NavigationMenu.nav_left_menu(browser, "Elements", "Check Box")
    CheckboxesRadiobuttons.expand_all(browser)
    yield


@pytest.fixture(autouse = True, scope = 'function')
@allure.title('Unchecking all the checkboxes after the test')
def uncheck_all(browser):
    """
    Fixture for unchecking all the selected checkboxes after each test end.
    """
    yield
    btn = 'Home'
    try:
        checked = CheckboxesRadiobuttons.find_all_checked_checkboxex(browser)
        halfchecked = CheckboxesRadiobuttons.find_all_halfchecked_checkboxes(browser)
        if btn in checked:
            CheckboxesRadiobuttons.find_checkbox_by_label(browser, btn)
        elif btn in halfchecked:
            CheckboxesRadiobuttons.find_checkbox_by_label(browser, btn)
            CheckboxesRadiobuttons.find_checkbox_by_label(browser, btn)
        else:
            pass
    except ValueError:
        pass
    finally:
        time.sleep(1)


dir_contents = {
    'Home': 'home desktop notes commands documents workspace react angular veu office public private classified general downloads wordFile excelFile',
    'Desktop': 'desktop notes commands',
    'Documents': 'documents workspace react angular veu office public private classified general',
    'WorkSpace': 'workspace react angular veu',
    'Office': 'office public private classified general',
    'Downloads': 'downloads wordFile excelFile',

}

dirs = ['Home', 'Desktop', 'Documents', 'WorkSpace', 'Office', 'Downloads']


@pytest.mark.parametrize('dir_names', dirs)
@allure.title('2.1 - Single checkbox selected')
@allure.description('Check the displayed folder contents after selecting a single checkbox')
@allure.tag('Elements', 'Checkboxes')
@allure.link(url = 'https://demoqa.com/checkbox')
def test_checkboxes_single_dir(browser, dir_names, request):
    with allure.step('Check single checkbox'):
        CheckboxesRadiobuttons.find_checkbox_by_label(browser, dir_names)
    with allure.step('Verify selected directory contents'):
        res = ' '.join(CheckboxesOutputs.get_output_for_checked_dir(browser))
        try:
            assert res == dir_contents[dir_names], f"The output result does not comply with " \
                                           f"the actual ({dir_names}) dir structure"
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f"The output result does not comply with " \
                                           f"the actual ({dir_names}) dir structure")


dirs2 = ['Documents', 'WorkSpace']
dirs3 = ['Desktop', 'Downloads']

@pytest.mark.parametrize('dir_names2', dirs2)
@pytest.mark.parametrize('dir_names3', dirs3)
@allure.title('2.2 - Multiple checkboxes selected')
@allure.description('Check the displayed folder(s) contents after selecting multiple checkboxes')
@allure.tag('Elements', 'Checkboxes')
@allure.link(url = 'https://demoqa.com/checkbox')
def test_checkboxes_mult_dirs(browser, dir_names2, dir_names3, request):
    with allure.step('Check multiple checkboxes'):
        CheckboxesRadiobuttons.find_checkbox_by_label(browser, dir_names2)
        CheckboxesRadiobuttons.find_checkbox_by_label(browser, dir_names3)
    with allure.step('Verify selected directories contents'):
        res = sorted(CheckboxesOutputs.get_output_for_checked_dir(browser))
        print(res)

        s_res = ' '.join(res)
        print('ACTUAL:', s_res)

        expected_res = dir_contents[dir_names2].split()
        adding_values = dir_contents[dir_names3].split()
        expected_res.extend(i for i in adding_values if i not in expected_res)
        expected_res.sort()
        print('EXPECTED:', ' '.join(expected_res))
        try:
            assert s_res == ' '.join(expected_res), f"The output result does not comply with " \
                                   f"the actual ({dir_names2}-{dir_names3}) dirs structure"
        except AssertionError:
            allure_screenshot_on_failure(browser, request)
            raise AssertionError(f"The output result does not comply with " \
                                   f"the actual ({dir_names2}-{dir_names3}) dirs structure")