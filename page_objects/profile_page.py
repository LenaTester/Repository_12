from selenium.webdriver.common.by import By

from pythonProject.Repository_3.framework_from_scratch.utilities.web_ui.base_page import BasePage
from pythonProject.Repository_3.framework_from_scratch.page_objects.new_email_page import NewEmailPage
from pythonProject.Repository_3.framework_from_scratch.page_objects.new_successful_password import NewSuccessfulPassword
from pythonProject.Repository_3.framework_from_scratch.utilities.decorators import auto_steps

@auto_steps
class ProfilePage(BasePage):
    __new_password = (By.XPATH, '//input[@name="n_password"]')
    __new_password_confirmation = (By.XPATH, '//input[@name="n_password_2"]')
    __save_button = (By.XPATH, '// input[ @ value = "сохранить"]')
    __new_email_field = (By.XPATH, '//input[@name="mail_new"]')
    __new_email_submit_button = (By.XPATH, '//input[@name="ml_submit"]')
    __notification_label_group = (By.XPATH, '//ul[@class="ul_user"]/child::li/child::b')
    __notification_label_comments = (By.XPATH, '//ul[@class="ul_user"]/child::li[2]/child::b')

    def __init__(self, driver):
        super().__init__(driver)

    def set_new_password(self, password):
        self.send_keys(self.__new_password, password)
        return self

    def set_new_password_confirmation(self, password):
        self.send_keys(self.__new_password_confirmation, password)
        return self

    def click_save_button(self):
        self.click(self.__save_button)
        return NewSuccessfulPassword(self._driver)

    def set_new_email(self, new_email):
        self.send_keys(self.__new_email_field, new_email)
        return self

    def email_submit_button(self):
        self.click(self.__new_email_submit_button)
        return NewEmailPage(self._driver)

    def get_notification_group(self):
        notification = self.wait_until_element_located(self.__notification_label_group)
        return self.get_text(notification)

    def get_notification_comments(self):
        notification = self.wait_until_element_located(self.__notification_label_comments)
        return self.get_text(notification)

