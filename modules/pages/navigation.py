import time

from selenium.common import ElementClickInterceptedException

from locators.navigation import NavigationLocators, TabsLocators
from modules.base import BasePage


class NavigationMenu(BasePage):

    def nav_left_menu(self, item_group: str, item_name: str):
        """
        The method works with the Navigation Menu located on the left side of the website.
        The menu consists of the menu groups and items located inside these groups (e.g.,
        the menu group Elements contains such items as Text Box, Check Box etc)
        If a group or an item is below the current page view, then the page will be scrolled down to it

        :param item_group: menu group text (dark grey color)
        :param item_name: menu item (light grey color)
        :return:
        """
        group = self.find_element(*NavigationLocators.get_menu_group_locator_by_text(item_group))
        name = self.find_element(*NavigationLocators.get_menu_item_locator_by_text(item_group, item_name))
        try:
            group.click()
            time.sleep(2)
            name.click()
            time.sleep(2)
            group.click()
            time.sleep(2)
        except ElementClickInterceptedException:
            self.execute_script("arguments[0].scrollIntoView();", name)
            time.sleep(2)
            name.click()
            time.sleep(2)
            group.click()
            time.sleep(2)

    def tabs_navigation(self, tabname: str):
        """
        Inner tabs navigation

        :param tabname: name of the tab to go to
        :return:
        """
        self.find_element(*TabsLocators.find_inline_tab_by_name(tabname)).click()
