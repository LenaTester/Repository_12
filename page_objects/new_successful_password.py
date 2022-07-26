from selenium.webdriver.common.by import By

from utilities.web_ui.base_page import BasePage
from utilities.decorators import auto_steps

@auto_steps
class NewSuccessfulPassword(BasePage):
    __notification_label = (By.XPATH, '//p[1]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_notification(self):
        notification = self.wait_until_element_located(self.__notification_label)
        return self.get_text(notification)
