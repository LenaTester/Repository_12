from selenium.webdriver.common.by import By

from pythonProject.Repository_3.framework_from_scratch.utilities.web_ui.base_page import BasePage
from pythonProject.Repository_3.framework_from_scratch.page_objects.profile_page import ProfilePage
from pythonProject.Repository_3.framework_from_scratch.page_objects.wrong_creds import WrongCreds
from pythonProject.Repository_3.framework_from_scratch.utilities.decorators import auto_steps

@auto_steps
class HomePage(BasePage):
    __email_input = (By.XPATH, '//*[@id="login"]')
    __password_input = (By.XPATH, '//*[@id="password"]')
    __login_button = (By.XPATH, '//*[contains(@name, "submit_enter")]')
    __page_a_button = (By.XPATH, '//div/a[text() = "А"]')
    __page_number_input = (By.XPATH, '//input[@name="p"]')
    __submit_page_button = (By.XPATH, '//input[@name="submit"]')
    __search_input = (By.XPATH, '//input[@name="search"]')
    __search_button = (By.XPATH, '//input[@value="Поиск"]')
    __profile_page_button = (By.XPATH, '//a[text() = "Личный кабинет"]')

    def __init__(self, driver):
        super().__init__(driver)

    def set_user_email(self, email):
        self.send_keys(self.__email_input, email)
        return self

    def set_password(self, password):
        self.send_keys(self.__password_input, password)
        return self

    def click_login_button(self):
        self.click(self.__login_button)
        return self

    def click_login_button_wrong_creds(self):
        self.click(self.__login_button)
        return WrongCreds(self._driver)

    def click_page_a_button(self):
        self.click(self.__page_a_button)
        return self

    def check_page_navigaion(self, page_number):
        self.send_keys(self.__page_number_input, page_number)
        return self

    def click_submit_button(self):
        self.click(self.__submit_page_button)
        return self

    def check_search(self, search_request):
        self.send_keys(self.__search_input, search_request)
        return self

    def click_search_button(self):
        self.click(self.__search_button)
        return self

    def click_profile_page_button(self):
        self.click(self.__profile_page_button)
        return ProfilePage(self._driver)



