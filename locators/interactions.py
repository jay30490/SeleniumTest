from selenium.webdriver.common.by import By


class InteractionsLocators:

    @staticmethod
    def sortable_list(item: str) -> tuple:
        return By.XPATH, f"//div[@id='demo-tabpane-list']/" \
                         f"descendant::div[contains(@class, 'list-group-item list-group-item-action') " \
                         f"and text() = '{item}']"

    @staticmethod
    def sortable_grid(item: str) -> tuple:
        return By.XPATH, f"//div[@id='demo-tabpane-grid']/" \
                         f"descendant::div[contains(@class, 'list-group-item list-group-item-action') " \
                         f"and text() = '{item}']"

    @staticmethod
    def selectable_list_partial_text(item: str) -> tuple:
        return By.XPATH, f"//ul[@id='verticalListContainer']/li[contains(text(), '{item}')]"

    @staticmethod
    def selectable_list_exact_text(item: str) -> tuple:
        return By.XPATH, f"//ul[@id='verticalListContainer']/li[text()='{item}']"

    @staticmethod
    def selectable_grid_partial_text(item: str) -> tuple:
        return By.XPATH, f"//div[@id='demo-tabpane-grid']/descendant::div/li[contains(text(), '{item}')]"

    @staticmethod
    def selectable_grid_exact_text(item: str) -> tuple:
        return By.XPATH, f"//div[@id='demo-tabpane-grid']/descendant::div/li[text()='{item}']"

    SELECTABLE_LIST_ITEMS = By.XPATH, "//ul[@id='verticalListContainer']/li"
    SELECTABLE_GRID_ITEMS = By.XPATH, "//div[@id='demo-tabpane-grid']/descendant::div/li"

    SORTABLE_LIST_ITEMS = By.XPATH, '//div[contains(@class, "vertical-list-container")]/div'
    SORTABLE_GRID_ITEMS = By.XPATH, '//div[@class = "create-grid"]/div'

    @staticmethod
    def selected_items_grid() -> tuple:
        return By.XPATH, f"//div[@id='demo-tabpane-grid']/" \
                         f"descendant::div/li[contains(@class, 'active')]"

    @staticmethod
    def selected_items_list() -> tuple:
        return By.XPATH, f"//ul[@id='verticalListContainer']/" \
                         f"li[contains(@class, 'active')]"

    RESIZABLE_BOX = By.ID, "resizableBoxWithRestriction"
    RESIZABLE_BOX_ARROW = By.XPATH, "//div[@id='resizableBoxWithRestriction']/span"

    DROPPABLE_DRAGBOX = By.ID, 'draggable'
    DROPPABLE_DROPBOX = By.ID, 'droppable'