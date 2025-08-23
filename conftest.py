# file for fixture and options
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# initialize func driver for tests
@pytest.fixture(scope="function", autouse=True) # open browser for each test, use auto in all tests
def driver(request):
    # create object options
    options = Options()
    # add options for browser
    # options.add_argument("--headless") # use headless for browser
    options.add_argument("--no-sandbox") # use no-sandbox
    options.add_argument('--disable-dev-shm-usage') # mast for docker - resolve memory problem
    options.add_argument('--disable-gpu') # disable GPU for tests
    options.add_argument('--start-maximized')  # fullscreen; use size for screen ("--window-size=1920x1080")
    driver = webdriver.Chrome(options=options) # use options in driver object
    request.cls.driver = driver # create object driver in tests class
    yield driver
    driver.quit()