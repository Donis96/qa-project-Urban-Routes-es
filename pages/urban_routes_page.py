from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


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
    blanket_and_tissues_checkbox = (By.CSS_SELECTOR,
                                    ".reqs-body > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    increase_ice_cream_button = (By.CSS_SELECTOR, "div.stepper-round__buttons > button:nth-child(3)")
    ice_cream_counter = (By.CSS_SELECTOR, ".stepper-round__counter")
    order_button = (By.CSS_SELECTOR, "button[type='submit']")
    taxi_search_modal = (By.CSS_SELECTOR, ".order-header-title")
    driver_name_info = (By.CSS_SELECTOR, ".order-info-element-text")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_route(self, from_address, to_address):
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.wait.until(EC.presence_of_element_located(self.from_field)).get_property('value')

    def get_to(self):
        return self.wait.until(EC.presence_of_element_located(self.to_field)).get_property('value')

    def click_personal_button(self):
        self.wait.until(EC.element_to_be_clickable(self.personal_button)).click()

    def select_comfort_rate(self):
        self.wait.until(EC.element_to_be_clickable(self.comfort_rate_button)).click()

    def comfort_rate_selected(self):
        element = self.wait.until(EC.presence_of_element_located(self.comfort_rate_button))
        return "active" in element.get_attribute("class")

    def fill_phone_number(self, phone_number):
        self.wait.until(EC.presence_of_element_located(self.phone_input_field)).send_keys(phone_number)
        self.wait.until(EC.element_to_be_clickable(self.next_button)).click()

    def submit_phone_code(self, code):
        self.wait.until(EC.presence_of_element_located(self.phone_code_input)).send_keys(code)
        self.wait.until(EC.element_to_be_clickable(self.next_button)).click()

    def add_credit_card(self, card_number, card_cvv):
        self.wait.until(EC.element_to_be_clickable(self.payment_method_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.add_card_link)).click()

        self.wait.until(EC.visibility_of_element_located(self.card_number_input))
        self.driver.find_element(*self.card_number_input).send_keys(card_number)

        self.driver.find_element(*self.card_cvv_input).send_keys(card_cvv)
        self.driver.find_element(*self.card_cvv_input).send_keys(Keys.TAB)

        self.wait.until(EC.element_to_be_clickable(self.link_card_button)).click()

    def write_message_for_driver(self, message):
        self.wait.until(EC.presence_of_element_located(self.message_input)).send_keys(message)

    def request_blanket_and_tissues(self):
        self.wait.until(EC.element_to_be_clickable(self.blanket_and_tissues_checkbox)).click()

    def blanket_and_tissues_selected(self):
        return self.wait.until(EC.presence_of_element_located(self.blanket_and_tissues_checkbox)).is_selected()

    def request_ice_cream(self, quantity):
        for _ in range(quantity - 1):
            self.wait.until(EC.element_to_be_clickable(self.increase_ice_cream_button)).click()

    def get_ice_cream_quantity(self):
        return int(self.wait.until(EC.presence_of_element_located(self.ice_cream_counter)).text)

    def click_order_button(self):
        self.wait.until(EC.element_to_be_clickable(self.order_button)).click()

    def wait_for_taxi_search_modal(self):
        self.wait.until(EC.visibility_of_element_located(self.taxi_search_modal))

    def wait_for_driver_info(self):
        self.wait.until(EC.visibility_of_element_located(self.driver_name_info))