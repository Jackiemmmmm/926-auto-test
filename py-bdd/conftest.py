import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from playwright.sync_api import sync_playwright


# update this part of code to use different option name or check if it already exists
def pytest_addoption(parser):
    # basic URL option
    if not any(opt.dest == "base_url" for opt in parser._anonymous.options):
        parser.addoption(
            "--base-url",
            action="store",
            default="http://localhost:5173",
            help="Base URL for the application under test",
        )

    # Selenium related options
    parser.addoption(
        "--chrome-path",
        action="store",
        default="chrome/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing",
        help="Path to Chrome binary",
    )
    parser.addoption(
        "--chromedriver-path",
        action="store",
        default="chrome/chromedriver-mac-arm64/chromedriver",
        help="Path to ChromeDriver",
    )
    # Playwright related options
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browsers in headless mode",
    )


# if use new option name, modify the fixture accordingly
@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url") or "http://localhost:5173"


# ------------ Selenium fixtures ------------ #


@pytest.fixture(scope="session")
def chrome_path(request):
    return request.config.getoption("--chrome-path")


@pytest.fixture(scope="session")
def chromedriver_path(request):
    return request.config.getoption("--chromedriver-path")


@pytest.fixture
def selenium_driver(chrome_path, chromedriver_path, request):
    """创建Selenium WebDriver实例"""
    # setup Chrome options
    chrome_options = Options()
    chrome_options.binary_location = chrome_path

    # acording to the command line argument, set headless mode
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")

    # setting the browser window size
    chrome_options.add_argument("--window-size=1280,720")

    # create a Service object
    service = Service(chromedriver_path)

    # create a webDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver

    # test finish, close the browser
    driver.quit()


# ------------ Playwright fixtures ------------ #


@pytest.fixture(scope="session")
def browser_type_launch_args(request):
    """define browser type launch arguments"""
    return {
        "headless": request.config.getoption("--headless"),
        "slow_mo": 100,  # slow down by 100ms
    }


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def playwright_browser(playwright, browser_type_launch_args):
    browser = playwright.chromium.launch(**browser_type_launch_args)
    yield browser
    browser.close()


@pytest.fixture
def playwright_context(playwright_browser):
    context = playwright_browser.new_context(viewport={"width": 1280, "height": 720})
    yield context
    context.close()


@pytest.fixture
def playwright_page(playwright_context, base_url):
    page = playwright_context.new_page()
    yield page
