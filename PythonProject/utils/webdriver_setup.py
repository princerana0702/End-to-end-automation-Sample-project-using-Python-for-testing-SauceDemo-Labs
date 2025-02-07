from selenium import webdriver
from config.config import config  # Import config JSON

def get_driver():
    """Initialize and return WebDriver"""
    options = webdriver.ChromeOptions()
    if config["headless"]:
        options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(config["timeout"])
    return driver
