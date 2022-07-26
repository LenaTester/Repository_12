from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def wait_until_element_located(self, locator):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait_until_element_located(locator)
        element.click()

    def get_text(self, element):
        return element.text

    def send_keys(self, locator, value, is_clear=False):
        element = self.wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    @property
    def title(self):
        return self._driver.title
