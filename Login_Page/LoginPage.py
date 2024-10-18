import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Login_Locator.LoginLocator import LoginLocator, LoginLocatorNegative, DeleteLoginLocator


class LoginPageNegative:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_email_address_fail(self, name):
        email_address = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocatorNegative.EMAIL_ADDRESS_FAIL))
        email_address.send_keys(name)
        time.sleep(2)

    def enter_password_fail(self, pass_word):
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocatorNegative.PASSWORD_FAIL))
        password.send_keys(pass_word)
        time.sleep(2)

    def click_submit_button_fail(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocatorNegative.SUBMIT_BUTTON_FAIL))
        submit_button.click()
        time.sleep(2)


class DeleteLoginPage:
    def __init__(self, driver):
        self.driver = driver

    def delete_failed_email_address(self, name):
        delete_email_address = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DeleteLoginLocator.DELETE_EMAIL_ADDRESS_FAIL))
        delete_email_address.clear()
        time.sleep(2)

    def delete_failed_password(self, pass_word):
        delete_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DeleteLoginLocator.DELETE_PASSWORD_FAIL))
        delete_password.clear()
        time.sleep(2)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_email_address(self, name):
        email_address = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.EMAIL_ADDRESS))
        email_address.send_keys(name)
        time.sleep(2)

    def enter_password(self, pass_word):
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.PASSWORD))
        password.send_keys(pass_word)
        time.sleep(2)

    def click_submit_button(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.SUBMIT_BUTTON))
        submit_button.click()
        time.sleep(2)
