import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.data import Data


class BaseTest:
    login_page: LoginPage
    dashboard_page: DashboardPage
    data: Data

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.data = Data()