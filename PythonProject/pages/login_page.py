from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import logger

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        try:
            logger.info(f"Attempting login with username: {username}")
            self.enter_text(self.USERNAME, username)
            self.enter_text(self.PASSWORD, password)
            self.click(self.LOGIN_BUTTON)
            logger.info("Login button clicked")
        except Exception as e:
            logger.error(f"Login failed due to error: {e}")
            self.take_screenshot("login_error")
            raise
