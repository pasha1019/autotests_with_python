import time
from os import login_tty

import config.links
import config.data
from selenium import webdriver


host = config.links.Links.HOST
login = config.data.Data.LOGIN
password = config.data.Data.PASSWORD
with webdriver.Chrome() as browser:
    browser.get(host)
    time.sleep(5)
    username_field = browser.find_element('xpath', "//input[@name='username']")
    pass_field = browser.find_element('xpath', "//input[@name='password']")
    login_button = browser.find_element('xpath', "//button[@type='submit']")
    username_field.clear()
    pass_field.clear()
    username_field.send_keys(login)
    pass_field.send_keys(password)
    time.sleep(5)
    login_button.click()
    time.sleep(5)
