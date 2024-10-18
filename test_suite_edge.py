import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

from Add_Contact_Page.AddContactPage import AddContactPage
from Config.Config import ConfigAddContact5, ConfigAddContact6, ConfigAddContact7, ConfigAddContact9, ConfigAddContact1, \
    ConfigAddContact4, ConfigAddContact3, ConfigAddContact2, ConfigLogin, ConfigAddContact10, \
    ConfigAddContact8, ConfigLoginNegative

from Login_Page.LoginPage import LoginPage, LoginPageNegative, DeleteLoginPage


# ----------------------------------------------------------------------------------------------------------------------
# HEADLESS MODE ON MICROSOFT EDGE BROWSER ------------------------------------------------------------------------------

@pytest.fixture(scope="session")
def driver_setup():
    edge_options = Options()
    # Uncomment the line below to run in headless mode
    edge_options.add_argument("--headless")  # Run Chrome in headless mode
    edge_options.add_argument("--disable-gpu")  # Optional: Disable GPU acceleration
    driver = webdriver.Edge(options=edge_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


# ----------------------------------------------------------------------------------------------------------------------
# HEADED MODE ON MICROSOFT EDGE BROWSER --------------------------------------------------------------------------------

# @pytest.fixture(scope="session")
# def driver_setup():
#     driver = webdriver.Edge()
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# ----------------------------------------------------------------------------------------------------------------------
# NEGATIVE TEST ON THE LOGIN PAGE --------------------------------------------------------------------------------------

@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url(ConfigLoginNegative.BaseUrl_FAIL)
    return login_page


def test_login_page_for_negative_contact_list_app(login):
    login_fail = LoginPageNegative(login.driver)
    login_fail.enter_email_address_fail(ConfigLoginNegative.EMAIL_ADDRESS_FAIL)
    login_fail.enter_password_fail(ConfigLoginNegative.PASSWORD_FAIL)
    login_fail.click_submit_button_fail()


def test_delete_login_page_contact_list_app(login):
    delete_login = DeleteLoginPage(login.driver)
    delete_login.delete_failed_email_address(ConfigLoginNegative.EMAIL_ADDRESS_FAIL)
    delete_login.delete_failed_password(ConfigLoginNegative.PASSWORD_FAIL)


# ----------------------------------------------------------------------------------------------------------------------
# POSITIVE TEST ON THE LOGIN PAGE --------------------------------------------------------------------------------------

def test_login_page_contact_list_app(login):
    login = LoginPage(login.driver)
    login.enter_email_address(ConfigLogin.EMAIL_ADDRESS)
    login.enter_password(ConfigLogin.PASSWORD)
    login.click_submit_button()


def test_add_contact_page_for_positive_test_contact_list_app(login):
    add_contact = AddContactPage(login.driver)

    # ----------------------------------------------------------------------------------------------------------------------
    # CONTACT ADDED --- 1 ----------------------------------------------------------------------------------------------

    add_contact.click_add_new_contact_button()
    add_contact.enter_first_name(ConfigAddContact1.FIRST_NAME)
    add_contact.enter_last_name(ConfigAddContact1.LAST_NAME)
    add_contact.enter_date_of_birth(ConfigAddContact1.DATE_OF_BIRTH)
    add_contact.enter_email_address(ConfigAddContact1.EMAIL_ADDRESS)
    add_contact.enter_phone_number(ConfigAddContact1.PHONE_NUMBER)
    add_contact.enter_street_address_one(ConfigAddContact1.STREET_ADDRESS_1)
    add_contact.enter_street_address_two(ConfigAddContact1.STREET_ADDRESS_2)
    add_contact.enter_city(ConfigAddContact1.CITY)
    add_contact.enter_state_province(ConfigAddContact1.STATE_PROVINCE)
    add_contact.enter_postal_code(ConfigAddContact1.POSTAL_CODE)
    add_contact.enter_country(ConfigAddContact1.COUNTRY)
    add_contact.click_submit_button()

    # ----------------------------------------------------------------------------------------------------------------------
    # CONTACT ADDED --- 2 ----------------------------------------------------------------------------------------------

    add_contact.click_add_new_contact_button()
    add_contact.enter_first_name(ConfigAddContact2.FIRST_NAME)
    add_contact.enter_last_name(ConfigAddContact2.LAST_NAME)
    add_contact.enter_date_of_birth(ConfigAddContact2.DATE_OF_BIRTH)
    add_contact.enter_email_address(ConfigAddContact2.EMAIL_ADDRESS)
    add_contact.enter_phone_number(ConfigAddContact2.PHONE_NUMBER)
    add_contact.enter_street_address_one(ConfigAddContact2.STREET_ADDRESS_1)
    add_contact.enter_street_address_two(ConfigAddContact2.STREET_ADDRESS_2)
    add_contact.enter_city(ConfigAddContact2.CITY)
    add_contact.enter_state_province(ConfigAddContact2.STATE_PROVINCE)
    add_contact.enter_postal_code(ConfigAddContact2.POSTAL_CODE)
    add_contact.enter_country(ConfigAddContact2.COUNTRY)
    add_contact.click_submit_button()

    # ----------------------------------------------------------------------------------------------------------------------
    # CONTACT ADDED --- 3 ----------------------------------------------------------------------------------------------

    add_contact.click_add_new_contact_button()
    add_contact.enter_first_name(ConfigAddContact3.FIRST_NAME)
    add_contact.enter_last_name(ConfigAddContact3.LAST_NAME)
    add_contact.enter_date_of_birth(ConfigAddContact3.DATE_OF_BIRTH)
    add_contact.enter_email_address(ConfigAddContact3.EMAIL_ADDRESS)
    add_contact.enter_phone_number(ConfigAddContact3.PHONE_NUMBER)
    add_contact.enter_street_address_one(ConfigAddContact3.STREET_ADDRESS_1)
    add_contact.enter_street_address_two(ConfigAddContact3.STREET_ADDRESS_2)
    add_contact.enter_city(ConfigAddContact3.CITY)
    add_contact.enter_state_province(ConfigAddContact3.STATE_PROVINCE)
    add_contact.enter_postal_code(ConfigAddContact3.POSTAL_CODE)
    add_contact.enter_country(ConfigAddContact3.COUNTRY)
    add_contact.click_submit_button()

    # ----------------------------------------------------------------------------------------------------------------------
    # CONTACT ADDED --- 4 ----------------------------------------------------------------------------------------------

    add_contact.click_add_new_contact_button()
    add_contact.enter_first_name(ConfigAddContact4.FIRST_NAME)
    add_contact.enter_last_name(ConfigAddContact4.LAST_NAME)
    add_contact.enter_date_of_birth(ConfigAddContact4.DATE_OF_BIRTH)
    add_contact.enter_email_address(ConfigAddContact4.EMAIL_ADDRESS)
    add_contact.enter_phone_number(ConfigAddContact4.PHONE_NUMBER)
    add_contact.enter_street_address_one(ConfigAddContact4.STREET_ADDRESS_1)
    add_contact.enter_street_address_two(ConfigAddContact4.STREET_ADDRESS_2)
    add_contact.enter_city(ConfigAddContact4.CITY)
    add_contact.enter_state_province(ConfigAddContact4.STATE_PROVINCE)
    add_contact.enter_postal_code(ConfigAddContact4.POSTAL_CODE)
    add_contact.enter_country(ConfigAddContact4.COUNTRY)
    add_contact.click_submit_button()

    # ----------------------------------------------------------------------------------------------------------------------
    # CONTACT ADDED --- 5 ----------------------------------------------------------------------------------------------

    add_contact.click_add_new_contact_button()
    add_contact.enter_first_name(ConfigAddContact5.FIRST_NAME)
    add_contact.enter_last_name(ConfigAddContact5.LAST_NAME)
    add_contact.enter_date_of_birth(ConfigAddContact5.DATE_OF_BIRTH)
    add_contact.enter_email_address(ConfigAddContact5.EMAIL_ADDRESS)
    add_contact.enter_phone_number(ConfigAddContact5.PHONE_NUMBER)
    add_contact.enter_street_address_one(ConfigAddContact5.STREET_ADDRESS_1)
    add_contact.enter_street_address_two(ConfigAddContact5.STREET_ADDRESS_2)
    add_contact.enter_city(ConfigAddContact5.CITY)
    add_contact.enter_state_province(ConfigAddContact5.STATE_PROVINCE)
    add_contact.enter_postal_code(ConfigAddContact5.POSTAL_CODE)
    add_contact.enter_country(ConfigAddContact5.COUNTRY)
    add_contact.click_submit_button()

    # ----------------------------------------------------------------------------------------------------------------------
    # CONTACT ADDED --- 6 ----------------------------------------------------------------------------------------------

    add_contact.click_add_new_contact_button()
    add_contact.enter_first_name(ConfigAddContact6.FIRST_NAME)
    add_contact.enter_last_name(ConfigAddContact6.LAST_NAME)
    add_contact.enter_date_of_birth(ConfigAddContact6.DATE_OF_BIRTH)
    add_contact.enter_email_address(ConfigAddContact6.EMAIL_ADDRESS)
    add_contact.enter_phone_number(ConfigAddContact6.PHONE_NUMBER)
    add_contact.enter_street_address_one(ConfigAddContact6.STREET_ADDRESS_1)
    add_contact.enter_street_address_two(ConfigAddContact6.STREET_ADDRESS_2)
    add_contact.enter_city(ConfigAddContact6.CITY)
    add_contact.enter_state_province(ConfigAddContact6.STATE_PROVINCE)
    add_contact.enter_postal_code(ConfigAddContact6.POSTAL_CODE)
    add_contact.enter_country(ConfigAddContact6.COUNTRY)
    add_contact.click_submit_button()

    # ----------------------------------------------------------------------------------------------------------------------
    # CONTACT ADDED --- 7 ----------------------------------------------------------------------------------------------

    add_contact.click_add_new_contact_button()
    add_contact.enter_first_name(ConfigAddContact7.FIRST_NAME)
    add_contact.enter_last_name(ConfigAddContact7.LAST_NAME)
    add_contact.enter_date_of_birth(ConfigAddContact7.DATE_OF_BIRTH)
    add_contact.enter_email_address(ConfigAddContact7.EMAIL_ADDRESS)
    add_contact.enter_phone_number(ConfigAddContact7.PHONE_NUMBER)
    add_contact.enter_street_address_one(ConfigAddContact7.STREET_ADDRESS_1)
    add_contact.enter_street_address_two(ConfigAddContact7.STREET_ADDRESS_2)
    add_contact.enter_city(ConfigAddContact7.CITY)
    add_contact.enter_state_province(ConfigAddContact7.STATE_PROVINCE)
    add_contact.enter_postal_code(ConfigAddContact7.POSTAL_CODE)
    add_contact.enter_country(ConfigAddContact7.COUNTRY)
    add_contact.click_submit_button()

    # ----------------------------------------------------------------------------------------------------------------------
    # CONTACT ADDED --- 8 ----------------------------------------------------------------------------------------------

    add_contact.click_add_new_contact_button()
    add_contact.enter_first_name(ConfigAddContact8.FIRST_NAME)
    add_contact.enter_last_name(ConfigAddContact8.LAST_NAME)
    add_contact.enter_date_of_birth(ConfigAddContact8.DATE_OF_BIRTH)
    add_contact.enter_email_address(ConfigAddContact8.EMAIL_ADDRESS)
    add_contact.enter_phone_number(ConfigAddContact8.PHONE_NUMBER)
    add_contact.enter_street_address_one(ConfigAddContact8.STREET_ADDRESS_1)
    add_contact.enter_street_address_two(ConfigAddContact8.STREET_ADDRESS_2)
    add_contact.enter_city(ConfigAddContact8.CITY)
    add_contact.enter_state_province(ConfigAddContact8.STATE_PROVINCE)
    add_contact.enter_postal_code(ConfigAddContact8.POSTAL_CODE)
    add_contact.enter_country(ConfigAddContact8.COUNTRY)
    add_contact.click_submit_button()

    # ----------------------------------------------------------------------------------------------------------------------
    # CONTACT ADDED --- 9 ----------------------------------------------------------------------------------------------

    add_contact.click_add_new_contact_button()
    add_contact.enter_first_name(ConfigAddContact9.FIRST_NAME)
    add_contact.enter_last_name(ConfigAddContact9.LAST_NAME)
    add_contact.enter_date_of_birth(ConfigAddContact9.DATE_OF_BIRTH)
    add_contact.enter_email_address(ConfigAddContact9.EMAIL_ADDRESS)
    add_contact.enter_phone_number(ConfigAddContact9.PHONE_NUMBER)
    add_contact.enter_street_address_one(ConfigAddContact9.STREET_ADDRESS_1)
    add_contact.enter_street_address_two(ConfigAddContact9.STREET_ADDRESS_2)
    add_contact.enter_city(ConfigAddContact9.CITY)
    add_contact.enter_state_province(ConfigAddContact9.STATE_PROVINCE)
    add_contact.enter_postal_code(ConfigAddContact9.POSTAL_CODE)
    add_contact.enter_country(ConfigAddContact9.COUNTRY)
    add_contact.click_submit_button()

    # ----------------------------------------------------------------------------------------------------------------------
    # CONTACT ADDED --- 10 ----------------------------------------------------------------------------------------------

    add_contact.click_add_new_contact_button()
    add_contact.enter_first_name(ConfigAddContact10.FIRST_NAME)
    add_contact.enter_last_name(ConfigAddContact10.LAST_NAME)
    add_contact.enter_date_of_birth(ConfigAddContact10.DATE_OF_BIRTH)
    add_contact.enter_email_address(ConfigAddContact10.EMAIL_ADDRESS)
    add_contact.enter_phone_number(ConfigAddContact10.PHONE_NUMBER)
    add_contact.enter_street_address_one(ConfigAddContact10.STREET_ADDRESS_1)
    add_contact.enter_street_address_two(ConfigAddContact10.STREET_ADDRESS_2)
    add_contact.enter_city(ConfigAddContact10.CITY)
    add_contact.enter_state_province(ConfigAddContact10.STATE_PROVINCE)
    add_contact.enter_postal_code(ConfigAddContact10.POSTAL_CODE)
    add_contact.enter_country(ConfigAddContact10.COUNTRY)
    add_contact.click_submit_button()
    add_contact.click_logout_button()
