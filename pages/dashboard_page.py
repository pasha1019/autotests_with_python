import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as ec


class DashboardPage(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE
    SEARCH = ("xpath", "//input[@class='oxd-input oxd-input--active']")

    @allure.step("Search is clickable")
    def search_is_click(self):
        self.wait.until(ec.element_to_be_clickable(self.SEARCH))