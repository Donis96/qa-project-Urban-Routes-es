from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    personal_button = (By.CSS_SELECTOR, ".modes-container .mode:nth-child(3)")
    comfort_rate_button = (By.CSS_SELECTOR, "div.tariff-card:nth-child(2)")
    phone_input_field = (By.ID, "phone")
    next_button = (By.CSS_SELECTOR, "button[type='submit']")
    phone_code_input = (By.ID, "code")
    payment_method_button = (By.CSS_SELECTOR, ".pp-button")
    add_card_link = (By.CSS_SELECTOR, ".pp-row.disabled")
    card_number_input = (By.ID, "number")
    card_cvv_input = (By.ID, "code")
    link_card_button = (By.CSS_SELECTOR, "div.pp-buttons-area button.button")
    message_input = (By.ID, "comment")
    blanket_and_tissues_checkbox = (By.CSS_SELECTOR, ".reqs-body > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    increase_ice_cream_button = (By.CSS_SELECTOR, "div.stepper-round__buttons > button:nth-child(3)")
    order_button = (By.CSS_SELECTOR, "button[type='submit']")
    taxi_search_modal = (By.CSS_SELECTOR, ".order-header-title")
    driver_name_info = (By.CSS_SELECTOR, ".order-info-element-text")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def set_from(self, from_address):
       #  self.driver.find_element(*self.from_field).send_keys(from_address)
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
       # self.driver.find_element(*self.to_field).send_keys(to_address)
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_personal_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.personal_button))

    def click_personal_button(self):
        self.get_personal_button().click()


def set_route(self, address_from, address_to):
    self.driver.find_element(*self.from_field).send_keys(address_from)
    self.driver.find_element(*self.to_field).send_keys(address_to)


def select_comfort_rate(self):
    self.driver.find_element(*self.comfort_rate_button).click()


def fill_phone_number(self, phone_number):
    self.driver.find_element(*self.phone_input_field).send_keys(phone_number)


def add_credit_card(self, card_number, card_cvv):
    self.driver.find_element(*self.payment_method_button).click()
    self.driver.find_element(*self.add_card_link).click()
    WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "number"))
    )

    self.driver.find_element(*self.card_number_input).send_keys(card_number)
    self.driver.find_element(*self.card_cvv_input).send_keys(card_cvv)
    self.driver.find_element(*self.card_cvv_input).send_keys(Keys.TAB)

    self.driver.find_element(*self.link_card_button).click()


def write_message_for_driver(self, message):
    self.driver.find_element(*self.message_input).send_keys(message)


def request_blanket_and_tissues(self):
    self.driver.find_element(*self.blanket_and_tissues_checkbox).click()


def request_ice_cream(self, quantity):
    for _ in range(quantity - 1):
        self.driver.find_element(*self.increase_ice_cream_button).click()


def click_order_button(self):
    self.driver.find_element(*self.order_button).click()


def wait_for_taxi_search_modal(self):
    return WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.taxi_search_modal)
    )


def wait_for_driver_info(self):
    return WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.driver_name_info)
    )
