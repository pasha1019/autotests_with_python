import time
import config.links
from selenium import webdriver


with webdriver.Chrome() as browser:
    browser.get(config.links.Links.HOST)
    time.sleep(5)
    username_field = browser.find_element('xpath', "//input[@name='username']")
    pass_field = browser.find_element('xpath', "//input[@name='password']")
    login_button = browser.find_element('xpath', "//button[@type='submit']")
    username_field.clear()
    pass_field.clear()
    username_field.send_keys('Admin')
    pass_field.send_keys('admin123')
    time.sleep(5)
    login_button.click()
    time.sleep(5)
