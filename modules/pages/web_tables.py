import pandas as pd
from selenium.common import NoSuchElementException
from typing import Literal

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from locators.web_tables import WebTablesLocators


class WebTables:

    def get_table_header(self) -> list:
        """
        Get all the headers of the web table

        :return: list of web table headers
        """
        return [i.text for i in self.find_elements(*WebTablesLocators.get_webtable_header())]

    def get_rows_num(self) -> int:
        """
        Get the number of rows in a web table

        :return: number of web table rows
        """
        return len(self.find_elements(*WebTablesLocators.get_webtable_contents_rows()))

    def get_tbl_contents(self) -> list:
        """
        Get the web table contents row by row in a list of dicts format

        :return: list of dicts where each dict is a web table row
                 with header as key and cell text as value
        """
        tbl_rows_each = self.find_elements(*WebTablesLocators.get_webtable_contents_rows())
        hdrs = [i.text for i in self.find_elements(*WebTablesLocators.get_webtable_header())]
        rows = [(i.text).split('\n') for i in tbl_rows_each]

        row_contents = []
        for row in rows:
            row_entries = {}
            for col, cell in zip(hdrs, row):
                row_entries[col] = cell
            row_contents.append(row_entries)
        df = pd.DataFrame.from_records(row_contents)
        return df.to_dict('records')


class WebTablesHandling:

    def change_row_count(self, row_count):
        """
        Change number of web table rows displayed on the page.
        This is a drop down list with the predefined values,
        however, it cannot be handled using the Select methods

        :param row_count: number of rows to be displayed
                          (should be the existing value from the drop down)
        :return:
        """
        sel = Select(self.find_element(*WebTablesLocators.ROWS_PER_PAGE))
        sel.select_by_visible_text(text = row_count)

    def search_field(self, search_text: str):
        """
        Enter a text into the Search field

        :param search_text: text to be entered
        :return:
        """
        search = self.find_element(*WebTablesLocators.SEARCH)
        search.click()
        search.send_keys(search_text)

    def clear_search_fld(self):
        """
        Clear the Search field

        :return:
        """
        search = self.find_element(*WebTablesLocators.SEARCH)
        search.click()
        search.clear()

    def sort_column(self, col_name: str, dbl_click: bool = False):
        """
        Sort the web table rows by a particular column.
        Single click - for ascending sorting
        Double click - for descending sorting
        By default, the sorting is performed in ascending order

        :param col_name: column name
        :param dbl_click: if the double click should be performed
        :return:
        """
        col = self.find_element(*WebTablesLocators.find_column_by_name(col_name))
        if dbl_click == True:
            ActionChains(self).double_click(col).perform()
        else:
            col.click()


class WebTablesEntries:

    def check_reg_form_open(self):
        """
        Check if the Registration Form is open

        :return: True if the form is open, otherwise False
        """
        try:
            self.find_element(*WebTablesLocators.REG_FORM_MODAL)
        except NoSuchElementException:
            return False
        else:
            return True

    def close_reg_form(self):
        """
        Close the Registration Form

        :return:
        """
        self.find_element(*WebTablesLocators.REG_FORM_CLOSE_BTN).click()


    _table_actions = Literal['Edit', 'Delete']

    def edit_delete_entry(self, first_name: str, last_name: str,
                   age: str, email: str, salary: str, department: str, action: str = _table_actions):
        """
        Find a row which should be edited or deleted and perform the action required

        :param first_name: value in the First Name column
        :param last_name: value in the Last Name column
        :param age: value in the Age column
        :param email: value in the Email column
        :param salary: value in the Salary column
        :param department: value in the Department column
        :param action: action to be performed (Edit or Delete)
        :return:
        """
        self.find_element(*WebTablesLocators.row_action(first_name = first_name,
                                                        last_name = last_name,
                                                        age = age,
                                                        email = email,
                                                        salary = salary,
                                                        department = department,
                                                        action = action)).click()
