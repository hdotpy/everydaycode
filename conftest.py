from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Browser to run tests against (chrome or firefox)")


@pytest.fixture(scope="session")
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        option = webdriver.ChromeOptions()
        option.add_argument("--incognito")
        option.add_argument("--start-maximized")
        option.add_argument("--no-sandbox")
        option.add_argument("disable-gpu")
        driver = webdriver.Chrome(options=option)
        driver.implicitly_wait(7)
    elif browser == "firefox":
        option = webdriver.FirefoxOptions()
        option.add_argument("--start-maximized")
        option.add_argument("--no-sandbox")
        option.add_argument("disable-gpu")
        driver = webdriver.Firefox(options=option)
        driver.implicitly_wait(7)
    else:
        raise ValueError(
            f"Browser '{browser}' is not supported. Use 'chrome' or 'firefox'.")

    yield driver
    driver.quit()
