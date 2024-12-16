import time

from selenium.webdriver import ActionChains

from locators.interactions import InteractionsLocators
from modules.base import BasePage


class Interactions(BasePage):

    def sort_list(self, item1: str, item2: str):
        """
        Move a list item from the Interaction - Sortable page (List tab)

        :param item1: item to move
        :param item2: item the position of which is to be replaced by item1
        :return:
        """
        src = self.find_element(*InteractionsLocators.sortable_list(item1))
        trg = self.find_element(*InteractionsLocators.sortable_list(item2))
        ActionChains(self).drag_and_drop(source = src, target = trg).perform()
        time.sleep(1)

    def sort_grid(self, item1: str, item2: str):
        """
        Move a grid item from the Interaction - Sortable page (Grid tab)

        :param item1: item to move
        :param item2: item the position of which is to be replaced by item1
        :return:
        """
        src = self.find_element(*InteractionsLocators.sortable_grid(item1))
        trg = self.find_element(*InteractionsLocators.sortable_grid(item2))
        ActionChains(self).drag_and_drop(source = src, target = trg).perform()
        time.sleep(1)

    def sort_list_get_items(self) -> list:
        """
        Get items list from the Interaction - Sortable page (List tab)

        :return: items list
        """
        list_items = self.find_elements(*InteractionsLocators.SORTABLE_LIST_ITEMS)
        return [i.text for i in list_items]

    def sort_grid_get_items(self) -> list:
        """
        Get items list from the Interaction - Sortable page (Grid tab)

        :return: items list
        """
        grid_items = self.find_elements(*InteractionsLocators.SORTABLE_GRID_ITEMS)
        return [i.text for i in grid_items]

    def select_list_exact_text(self, *args):
        """
        Select items on the list from the Interaction - Sortable page (List tab)

        :param args: text of items to be selected
        :return:
        """
        for i in args:
            self.find_element(*InteractionsLocators.selectable_list_exact_text(i)).click()

    def select_grid_exact_text(self, *args):
        """
        Select items on the list from the Interaction - Sortable page (Grid tab)

        :param args: text of items to be selected
        :return:
        """
        for i in args:
            self.find_element(*InteractionsLocators.selectable_grid_exact_text(i)).click()

    def get_selected_list_items(self) -> list:
        """
        Get the list of selected items from the Interaction - Sortable page (List tab)

        :return: selected items list
        """
        return [i.text for i in self.find_elements(*InteractionsLocators.selected_items_list())]

    def get_selected_grid_items(self) -> list:
        """
        Get the list of selected items from the Interaction - Sortable page (Grid tab)

        :return: selected items list
        """
        return [i.text for i in self.find_elements(*InteractionsLocators.selected_items_grid())]

    def resize_box_get_size(self) -> tuple:
        """
        Get width and height of the resizable box located at the top of Interaction - Resizable page

        :return: a tuple containing the box width and height
        """
        box = self.find_element(*InteractionsLocators.RESIZABLE_BOX)
        return (box.value_of_css_property('width'), \
               box.value_of_css_property('height'))

    def resize_box_change_size(self, xoffset: int, yoffset: int):
        """
        Change width and height of the resizable box located at the top of Interaction - Resizable page

        :param xoffset: difference (in pixels) between the new and old width.
                        Should be negative in case of decreasing the size
        :param yoffset: difference (in pixels) between the new and old height.
                        Should be negative in case of decreasing the size
        :return:
        """
        arrow = self.find_element(*InteractionsLocators.RESIZABLE_BOX_ARROW)
        ActionChains(self).click_and_hold(arrow). \
            drag_and_drop_by_offset(arrow, xoffset = xoffset, yoffset = yoffset). \
            release(). \
            perform()

    def droppable_simple(self):
        """
        Drag the draggable box into the drop box on the Interaction - Droppable page

        :return:
        """
        dragbox = self.find_element(*InteractionsLocators.DROPPABLE_DRAGBOX)
        dropbox = self.find_element(*InteractionsLocators.DROPPABLE_DROPBOX)
        ActionChains(self).drag_and_drop(dragbox, dropbox).perform()

    def get_drop_text(self) -> str:
        """
        Get text of the drop box from the Interaction - Droppable page

        :return: text displayed on the drop box
        """
        return self.find_element(*InteractionsLocators.DROPPABLE_DROPBOX).text
