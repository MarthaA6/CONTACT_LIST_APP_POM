from selenium.webdriver.common.by import By


class LoginLocator:
    EMAIL_ADDRESS = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
