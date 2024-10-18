from selenium.webdriver.common.by import By


class LoginLocatorNegative:
    EMAIL_ADDRESS_FAIL = (By.ID, "email")
    PASSWORD_FAIL = (By.ID, "password")
    SUBMIT_BUTTON_FAIL = (By.ID, "submit")


class DeleteLoginLocator:
    DELETE_EMAIL_ADDRESS_FAIL = (By.ID, "email")
    DELETE_PASSWORD_FAIL = (By.ID, "password")


class LoginLocator:
    EMAIL_ADDRESS = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
