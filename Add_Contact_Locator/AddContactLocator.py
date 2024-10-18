from selenium.webdriver.common.by import By


class AddContactLocator:
    ADD_NEW_CONTACT_BUTTON = (By.ID, "add-contact")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    DATE_OF_BIRTH = (By.ID, "birthdate")
    EMAIL_ADDRESS = (By.ID, "email")
    PHONE_NUMBER = (By.ID, "phone")
    STREET_ADDRESS_1 = (By.ID, "street1")
    STREET_ADDRESS_2 = (By.ID, "street2")
    CITY = (By.ID, "city")
    STATE_PROVINCE = (By.ID, "stateProvince")
    POSTAL_CODE = (By.ID, "postalCode")
    COUNTRY = (By.ID, "country")
    SUBMIT_BUTTON = (By.ID, "submit")
    LOGOUT_BUTTON = (By.ID, "logout")
