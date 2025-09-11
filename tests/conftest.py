import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = None


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    """
    Add custom command-line option to select browser type.

    Example usage:
        pytest --browser_name=chrome
    """
    parser.addoption("--browser_name", action="store", default="firefox")


@pytest.fixture(scope="class")
def setup(request):
    """
    Class-level setup fixture to initialize the browser.

    Sets up WebDriver, opens the URL, maximizes window,
    and assigns driver to the test class.
    """
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="function")
def browserInstance(request):
    """
    Function-level fixture to initialize browser per test function.

    Provides isolated browser instance with implicit wait and
    browser options as needed.
    """
    global driver
    browser_name = request.config.getoption("browser_name") or "firefox"

    if browser_name == "chrome":
        # ✅ Add Chrome options to disable password manager
        chrome_options = Options()
        chrome_options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
            },
        )
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    elif browser_name == "firefox":
        service_obj = FirefoxService()
        driver = webdriver.Firefox(service=service_obj)

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver  # Before test function execution
    driver.close()  # After test function execution


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
            file_name = os.path.join(
                reports_dir, report.nodeid.replace("::", "_") + ".png"
            )
            print("file name is " + file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = (
                    '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
                )
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(file_name):
    """
    Helper function to capture screenshot and save to given file path.

    Args:
        file_name (str): Path where the screenshot will be saved
    """
    driver.get_screenshot_as_file(file_name)
