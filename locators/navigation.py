from selenium.webdriver.common.by import By


class NavigationLocators:
    # Locators for the navigation menu

    LEFT_MENU_CLICKABILITY = By.XPATH, '//div[@class="left-pannel"]/descendant::div[text()="Elements"]'

    @staticmethod
    def get_menu_group_locator_by_text(item_group: str) -> tuple:
        return By.XPATH, f'//div[@class="left-pannel"]/descendant::div[text()="{item_group}"]'

    @staticmethod
    def get_menu_item_locator_by_text(item_group: str, item_name: str) -> tuple:
        """
        Get locator for a left menu item by its group and text

        :param item_group: parent group of the item
        :param item_name: menu item name
        :return: locator of the left menu item
        """
        return By.XPATH, f'//div[@class="left-pannel"]/descendant::div[text()="{item_group}"]/' \
                         f'following::span[text()="{item_name}"]'

    @staticmethod
    def check_if_menu_open(item_group: str) -> tuple:
        return By.XPATH, f'//div[@class="left-pannel"]/descendant::div[text()="{item_group}"]/' \
                         'following::div[contains(@class,"element-list collapse show")]'


class TabsLocators:

    @staticmethod
    def find_inline_tab_by_name(tabname: str):
        return By.XPATH, f"//a[text()='{tabname}']"

    SORTABLE_GRID = By.ID, "demo-tab-grid"
