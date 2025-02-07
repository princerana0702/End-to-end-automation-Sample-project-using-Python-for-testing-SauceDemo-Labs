from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from exceptions.custom_exceptions import ElementNotFoundException
from utils.logger import logger
import os

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find_element(self, locator):
        try:
            logger.info(f"Finding element: {locator}")
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Timeout: Element not found {locator}")
            raise ElementNotFoundException(f"Element not found: {locator}")
        except NoSuchElementException:
            logger.error(f"Error: No such element {locator}")
            raise ElementNotFoundException(f"Element not found: {locator}")

    def click(self, locator):
        logger.info(f"Clicking on element: {locator}")
        try:
            self.find_element(locator).click()
        except Exception as e:
            logger.error(f"Error clicking element: {locator}, {e}")
            self.take_screenshot("click_error")
            raise

    def enter_text(self, locator, text):
        logger.info(f"Entering text '{text}' in {locator}")
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            logger.error(f"Error entering text in {locator}, {e}")
            self.take_screenshot("input_error")
            raise

    def take_screenshot(self, name):
        """Takes a screenshot and saves it in screenshots folder"""
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = f"screenshots/{name}.png"
        self.driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved: {screenshot_path}")
