import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from data.data import urban_routes_url, address_from, address_to
from pages import urban_routes_page as urp
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.driver.get(urban_routes_url)
        self.routes_page = urp.UrbanRoutesPage(self.driver)

    def test_set_route(self):
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_comfort_rate(self):
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.select_comfort_rate()
        assert self.routes_page.comfort_rate_selected()

    def test_phone_number(self):
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.fill_phone_number('+1 123 123 12 12')
        modal_title_locator = (By.CLASS_NAME, "modal-header")
        try:
            modal_title = self.routes_page.wait.until(EC.visibility_of_element_located(modal_title_locator)).text
            assert "Ingresar el código" in modal_title
        except TimeoutException:
            pytest.fail("El modal de código de confirmación no apareció.")

    def test_add_card(self):
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.fill_phone_number('+1 123 123 12 12')
        self.routes_page.add_credit_card('1234567890123456', '111')
        payment_method_selected = (By.CSS_SELECTOR, "div.pp-button.selected")
        try:
            assert self.routes_page.wait.until(EC.visibility_of_element_located(payment_method_selected))
        except TimeoutException:
            pytest.fail("La tarjeta de crédito no fue seleccionada.")

    def test_message_for_driver(self):
        self.routes_page.set_route(address_from, address_to)
        message = 'Muéstrame el museo'
        self.routes_page.write_message_for_driver(message)
        assert self.routes_page.wait.until(EC.presence_of_element_located(self.routes_page.message_input)).get_attribute("value") == message

    def test_request_blanket_and_tissues(self):
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.request_blanket_and_tissues()
        assert self.routes_page.blanket_and_tissues_selected()

    def test_request_ice_cream(self):
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.request_ice_cream(2)
        assert self.routes_page.get_ice_cream_quantity() == 2

    def test_modal_for_taxi_search(self):
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_order_button()
        self.routes_page.wait_for_taxi_search_modal()
        modal_text = self.driver.find_element(*self.routes_page.taxi_search_modal).text
        assert "Búsqueda de taxi" in modal_text

    def test_driver_info_modal(self):
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_order_button()
        self.routes_page.wait_for_taxi_search_modal()
        self.routes_page.wait_for_driver_info()
        driver_name = self.driver.find_element(*self.routes_page.driver_name_info).text
        assert driver_name != ""

    def test_option(self):
        self.routes_page.click_personal_button()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
