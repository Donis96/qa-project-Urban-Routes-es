from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import data
from utils import retrieve_code
import time
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    pedir_un_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_button = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    confirm_comfort_option = (By.XPATH, '//div[@class="r-sw-label" and text()= "Manta y pañuelos"]')
    phone_number_button = (By.CSS_SELECTOR, ".np-button")
    phone_number_field = (By.ID, "phone")
    siguiente_button = (By.CSS_SELECTOR, "button.button.full")
    sms_code_field = (By.ID, "code")
    confirm_code_button = (By.XPATH, "//div[@class='buttons']/button[text()='Confirmar']")
    #prueba tajeta de credito
    payment_method_button = (By.CSS_SELECTOR, ".pp-value-arrow")
    add_card_option = (By.CSS_SELECTOR, ".pp-plus-container")
    card_number_field = (By.ID, "number")
    card_code_field = (By.NAME, "code")
    card_submit_button = (By.XPATH, "//div[@class='pp-buttons']/button[text()='Agregar']")
    card = (By.XPATH, "//div[@class='pp-title' and text()='Tarjeta']")
    payment_close_button = (By.XPATH, "//div[@class='payment-picker open']//button[@class='close-button section-close']")
    message_for_driver_field = (By.ID, "comment")
    blanket_and_scarves_option = (By.XPATH, "//div[text()='Manta y pañuelos']/following-sibling::div[@class='r-sw']//span[@class='slider round']")
    blanket_and_scarves_input = (By.CLASS_NAME, 'switch-input')
    ice_cream_button = (By.XPATH, "//div[text()='Helado']/following-sibling::div[@class='r-counter']//div[@class='counter-plus']")
    number_ice_cream = (By.CLASS_NAME, 'counter-value')
    order_taxi_button = (By.XPATH, "//button[contains(@class, 'smart-button') and .//span[text()='Pedir un taxi']]")
    request_confirmation = (By.CLASS_NAME, 'order-header-title')



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)


    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
       #self.driver.find_element(*self.to_field).send_keys(to_address)
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_pedir_un_taxi_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.pedir_un_taxi_button))

    def click_on_pedir_un_taxi_button(self):
        self.get_pedir_un_taxi_button().click()

    def get_comfort_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.comfort_button))

    def click_on_comfort_button(self):
        self.get_comfort_button().click()

    def get_confirm_comfort_option(self):
        return self.wait.until(EC.presence_of_element_located(self.confirm_comfort_option)).text

    def get_click_on_phone_number_button(self):
       return self.wait.until(EC.presence_of_element_located(self.phone_number_button))

    def click_on_phone_number_button(self):
        self.get_click_on_phone_number_button().click()

    def get_phone_number_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_number_field))

    def set_phone_number(self):
        self.get_phone_number_field().send_keys(data.phone_number)

    def get_siguiente_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.siguiente_button))

    def click_on_siguiente_button(self):
        self.get_siguiente_button().click()

    def get_sms_code_field(self):
        return self.wait.until(EC.presence_of_element_located(self.sms_code_field))

    def set_sms_code(self):
        self.get_sms_code_field().send_keys(retrieve_code.retrieve_phone_code(self.driver))

    def get_confirm_sms_code(self):
        return self.wait.until(EC.element_to_be_clickable(self.confirm_code_button))

    def set_confirm_sms_code(self):
        self.get_confirm_sms_code().click()

    def get_logged_in_phone_field(self):
        phone_element = self.wait.until(EC.presence_of_element_located(self.phone_number_field))
        return phone_element.get_attribute('value').strip()


    def get_payment_method_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.payment_method_button))

    def click_payment_method(self):
        self.get_payment_method_button().click()

    def get_add_card_option(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card_option))

    def set_add_card_option(self):
        self.get_add_card_option().click()

    def get_card_number_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.card_number_field))

    def set_card_number(self):
        self.get_card_number_field().send_keys(data.card_number)

    def get_card_code_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.card_code_field))

    def set_card_code(self):
        self.get_card_code_field().send_keys(data.card_code)

    def get_card_submit_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.card_submit_button))

    def set_card_submit_button(self):
        self.get_card_submit_button().click()

    def get_card(self):
        return self.wait.until(EC.presence_of_element_located(self.card))

    def get_payment_close_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.payment_close_button))

    def set_payment_close_button(self):
        self.get_payment_close_button().click()

    def get_message_for_driver_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.message_for_driver_field))

    def set_message_for_driver_field(self):
        message = data.message_for_driver
        self.get_message_for_driver_field().send_keys(message)

    def get_blanket_and_scarves(self):
        return self.wait.until(EC.element_to_be_clickable(self.blanket_and_scarves_option))

    def set_blanket_and_scarves_option(self):
        self.get_blanket_and_scarves().click()

    def get_blanket_and_scarves_input(self):
        return self.wait.until(EC.presence_of_element_located(self.blanket_and_scarves_input))

    def get_ice_cream_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.ice_cream_button))

    def set_ice_cream_button(self, ice_cream_number):
        for ice_cream in range (ice_cream_number):
            self.get_ice_cream_button().click()

    def get_ice_cream_number(self):
        return self.wait.until(EC.presence_of_element_located(self.number_ice_cream))

    def get_order_taxi_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.order_taxi_button))

    def set_order_taxi_button(self):
        tiempo = 27
        self.get_order_taxi_button().click()
        for segundo in range(tiempo):
            print(f"Tiempo, {segundo} segundos de espera.")
            time.sleep(1)


    def get_request_confirmation(self):
        return self.wait.until(EC.presence_of_element_located(self.request_confirmation))