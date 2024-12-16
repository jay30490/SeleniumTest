from selenium.webdriver.common.by import By


class WebTablesLocators:

    @staticmethod
    def get_webtable_header() -> tuple:
        return By.XPATH, "//div[contains(@class, 'ReactTable')]/" \
                         "descendant::div[contains(@class, 'rt-resizable-header-content')]"

    @staticmethod
    def find_column_by_name(col_name) -> tuple:
        return By.XPATH, f"//div[contains(@class, 'ReactTable')]/" \
                         f"descendant::div[contains(@class, 'rt-resizable-header-content') " \
                         f"and text() = '{col_name}']"

    @staticmethod
    def get_webtable_contents_rows() -> tuple:
        return By.XPATH, "//div[contains(@class, 'ReactTable')]/" \
                         "descendant::div[contains(@class, 'rt-tbody')]/" \
                         "descendant::div[contains(@class, 'rt-tr-group')]"

    @staticmethod
    def get_webtable_contents_cols() -> tuple:
        return By.XPATH, "//div[contains(@class, 'ReactTable')]/" \
                         "descendant::div[contains(@class, 'rt-tbody')]/" \
                         "descendant::div[contains(@class, 'rt-tr-group')]/" \
                         "descendant::div[contains(@class, 'rt-td')]"

    @staticmethod
    def get_webtable_contents_cells() -> tuple:
        return By.XPATH, "//div[contains(@class, 'ReactTable')]/" \
                         "descendant::div[contains(@class, 'rt-tbody')]/" \
                         "descendant::div[contains(@class, 'rt-tr-group')]/" \
                         "descendant::div[contains(@class, 'rt-td')]"

    @staticmethod
    def row_action(first_name: str, last_name: str,
                   age: str, email: str, salary: str, department: str, action: str) -> tuple:
        return By.XPATH, f'//div[@role="row"]/div[text()="{first_name}"]/' \
                         f'following-sibling::div[text()="{last_name}"]/' \
                         f'following-sibling::div[text()="{age}"]/' \
                         f'following-sibling::div[text()="{email}"]/' \
                         f'following-sibling::div[text()="{salary}"]/' \
                         f'following-sibling::div[text()="{department}"]/' \
                         f'following-sibling::div[@role="gridcell"]/' \
                         f'div[@class="action-buttons"]/' \
                         f'span[@title="{action}"]'

    ROWS_PER_PAGE = By.XPATH, '//select[@aria-label = "rows per page"]'
    SEARCH = By.ID, 'searchBox'
    REG_FORM_MODAL = By.ID, 'registration-form-modal'
    REG_FORM_CLOSE_BTN = By.XPATH, '//div[@role="document"]/descendant::div[text()="Registration Form"]/' \
                                   'following-sibling::button[@class="close"]'
    EDIT_BTN = By.XPATH, '//div[@class="action-buttons"]/span[@title="Edit"]'
    DELETE_BTN = By.XPATH, '//div[@class="action-buttons"]/span[@title="Delete"]'
