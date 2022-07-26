from contextlib import suppress
import allure
import pytest

from pythonProject.Repository_3.framework_from_scratch.page_objects.home_page import HomePage
from pythonProject.Repository_3.framework_from_scratch.utilities.driver_factory import DriverFactory
from pythonProject.Repository_3.framework_from_scratch.utilities.read_run_settings import ReadConfig

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture()
def create_driver(request):
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id(), is_headless=ReadConfig.get_headless_mod())
    driver.get('http://loveread.ec/')
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()

@pytest.fixture()
def get_home_page(create_driver):
    return HomePage(create_driver)

@pytest.fixture()
def successful_login(get_home_page, create_driver):
    home_page = get_home_page
    user_page = home_page.set_user_email('OlenaL').set_password('VTfRkcJVNi').click_login_button()
    return user_page

@pytest.fixture()
def non_successful_login_wrong_login(get_home_page, create_driver):
    home_page = get_home_page
    WrongCreds = home_page.set_user_email('Natasha').set_password('VTfRkcJVNi').click_login_button_wrong_creds()
    return WrongCreds

@pytest.fixture()
def non_successful_login_wrong_password(get_home_page, create_driver):
    home_page = get_home_page
    WrongCreds = home_page.set_user_email('OlenaL').set_password('OlenaL').click_login_button_wrong_creds()
    return WrongCreds

@pytest.fixture()
def successful_login_go_to_profile(get_home_page, create_driver):
    home_page = get_home_page
    ProfilePage = home_page.set_user_email('OlenaL').set_password('VTfRkcJVNi').click_login_button().click_profile_page_button()
    return ProfilePage

@pytest.fixture()
def new_pass(successful_login_go_to_profile, create_driver):
    profile_page = successful_login_go_to_profile
    NewSuccessfulPassword = profile_page.set_new_password('VTfRkcJVNi').set_new_password_confirmation('VTfRkcJVNi').click_save_button()
    return NewSuccessfulPassword

@pytest.fixture()
def new_email(successful_login_go_to_profile, create_driver):
    profile_page = successful_login_go_to_profile
    NewEmailPage = profile_page.set_new_email('elena.liashchenko03103@gmail.com').email_submit_button()
    return NewEmailPage

@pytest.fixture()
def new_wrong_email(successful_login_go_to_profile, create_driver):
    profile_page = successful_login_go_to_profile
    user_page = profile_page.set_new_email('test').email_submit_button()
    return user_page