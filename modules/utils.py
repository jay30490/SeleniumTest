import allure


def allure_screenshot_on_failure(browser, request):
    allure.attach(browser.get_screenshot_as_png(),
                  name = request.node.originalname,
                  attachment_type = allure.attachment_type.PNG)