import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Profile Functionality") #group tests in report
class TestProfileFeature(BaseTest):
    @allure.title("Login in profile") # name of test
    @allure.severity("CRITICAL") # category of test
    @pytest.mark.smoke # mark for filter
    def test_login_in_profile(self):
        self.login_page.open()  # open login page
        self.login_page.enter_login(self.data.LOGIN)  # login
        self.login_page.enter_password(self.data.PASSWORD)    # password
        self.login_page.click_submit_button()  # click button
        self.dashboard_page.is_opened()
        self.dashboard_page.search_is_click()
        self.dashboard_page.make_screenshot("Success")