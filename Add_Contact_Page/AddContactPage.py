import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Add_Contact_Locator.AddContactLocator import AddContactLocator


class AddContactPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact_button(self):
        add_new_contact_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.ADD_NEW_CONTACT_BUTTON))
        add_new_contact_button.click()
        time.sleep(2)

    def enter_first_name(self, first):
        first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.FIRST_NAME))
        first_name.send_keys(first)
        time.sleep(2)

    def enter_last_name(self, last):
        last_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.LAST_NAME))
        last_name.send_keys(last)
        time.sleep(2)

    def enter_date_of_birth(self, date):
        date_of_birth = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.DATE_OF_BIRTH))
        date_of_birth.send_keys(date)
        time.sleep(2)

    def enter_email_address(self, email):
        emai_address = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.EMAIL_ADDRESS))
        emai_address.send_keys(email)
        time.sleep(2)

    def enter_phone_number(self, number):
        phone_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.PHONE_NUMBER))
        phone_number.send_keys(number)
        time.sleep(2)

    def enter_street_address_one(self, address_one):
        stree_address_one = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.STREET_ADDRESS_1))
        stree_address_one.send_keys(address_one)
        time.sleep(3)

    def enter_street_address_two(self, address_two):
        stree_address_two = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.STREET_ADDRESS_2))
        stree_address_two.send_keys(address_two)
        time.sleep(2)

    def enter_city(self, place):
        city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.CITY))
        city.send_keys(place)
        time.sleep(2)

    def enter_state_province(self, state):
        phone_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.STATE_PROVINCE))
        phone_number.send_keys(state)
        time.sleep(2)

    def enter_postal_code(self, code):
        postal_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.POSTAL_CODE))
        postal_code.send_keys(code)
        time.sleep(2)

    def enter_country(self, location):
        country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.COUNTRY))
        country.send_keys(location)
        time.sleep(2)

    def click_submit_button(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.SUBMIT_BUTTON))
        submit_button.click()
        time.sleep(2)

    def click_logout_button(self):
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddContactLocator.LOGOUT_BUTTON))
        logout_button.click()
        time.sleep(2)
