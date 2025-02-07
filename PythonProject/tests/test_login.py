import pytest
from utils.webdriver_setup import get_driver
from pages.login_page import LoginPage
from config.config import config, testdata
from utils.logger import logger
import os


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def take_test_screenshot(driver, test_name):
    os.makedirs("screenshots", exist_ok=True)
    screenshot_path = f"screenshots/{test_name}.png"
    driver.save_screenshot(screenshot_path)
    logger.info(f"Screenshot saved: {screenshot_path}")


def test_valid_login(driver):
    logger.info("===== Starting test: test_valid_login =====")
    try:
        login_page = LoginPage(driver)

        logger.info("Opening SauceDemo login page")
        login_page.open_url(config["base_url"])

        logger.info(f"Entering username: {testdata['valid_login']['username']}")
        logger.info(f"Entering password: {'*' * len(testdata['valid_login']['password'])}")  # Hide actual password
        login_page.login(testdata["valid_login"]["username"], testdata["valid_login"]["password"])

        logger.info("Checking if login is successful")
        assert "inventory" in driver.current_url, "Login failed!"

        logger.info("Test Passed: test_valid_login")
    except Exception as e:
        logger.error(f"Test Failed: test_valid_login, Error: {e}")
        take_test_screenshot(driver, "test_valid_login")
        raise


def test_invalid_login(driver):
    logger.info("===== Starting test: test_invalid_login =====")
    try:
        login_page = LoginPage(driver)
        login_page.open_url(config["base_url"])

        logger.info("Entering invalid username and password")
        login_page.login(testdata["invalid_login"]["username"], testdata["invalid_login"]["password"])

        logger.info("Checking if error message is displayed")
        assert "Epic sadface" in driver.page_source, "Error message not displayed!"

        logger.info("Test Passed: test_invalid_login")
    except Exception as e:
        logger.error(f"Test Failed: test_invalid_login, Error: {e}")
        take_test_screenshot(driver, "test_invalid_login")
        raise

# Test - Blank Username & Password
def test_blank_username_password(driver):
    logger.info("===== Starting test: test_blank_username_password =====")
    try:
        login_page = LoginPage(driver)
        login_page.open_url(config["base_url"])

        logger.info("Submitting login form with blank username & password")
        login_page.login("", "")

        logger.info("Checking if blank error message is displayed")
        assert "Epic sadface" in driver.page_source, "Error message not displayed!"

        logger.info("Test Passed: test_blank_username_password")
    except Exception as e:
        logger.error(f"Test Failed: test_blank_username_password, Error: {e}")
        take_test_screenshot(driver, "test_blank_username_password")
        raise

# Test - Blank Password Only
def test_blank_password(driver):
    logger.info("===== Starting test: test_blank_password =====")
    try:
        login_page = LoginPage(driver)
        login_page.open_url(config["base_url"])

        logger.info("Entering username but leaving password blank")
        login_page.login(testdata["valid_login"]["username"], "")

        logger.info("Checking if blank password error message is displayed")
        assert "Epic sadface" in driver.page_source, "Error message not displayed!"

        logger.info("Test Passed: test_blank_password")
    except Exception as e:
        logger.error(f"Test Failed: test_blank_password, Error: {e}")
        take_test_screenshot(driver, "test_blank_password")
        raise

# Test - Blank Username Only
def test_blank_username(driver):
    logger.info("===== Starting test: test_blank_username =====")
    try:
        login_page = LoginPage(driver)
        login_page.open_url(config["base_url"])

        logger.info("Entering password but leaving username blank")
        login_page.login("", testdata["valid_login"]["password"])

        logger.info("Checking if blank username error message is displayed")
        assert "Epic sadface" in driver.page_source, "Error message not displayed!"

        logger.info("Test Passed: test_blank_username")
    except Exception as e:
        logger.error(f"Test Failed: test_blank_username, Error: {e}")
        take_test_screenshot(driver, "test_blank_username")
        raise