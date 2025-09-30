from data import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages import urban_routes_page as urp
from selenium.webdriver import Keys


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)


    def test_urban_routes(self):
        self.driver.get(data.urban_routes_url)
        routes_page = urp.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_options(self):
        self.routes_page.click_on_pedir_un_taxi_button()
        comfort_rate = self.routes_page.get_comfort_button().text
        assert comfort_rate == 'Comfort'

    def test_tariffs(self):
        self.routes_page.click_on_comfort_button()
        confirmation = self.routes_page.get_confirm_comfort_option()
        assert confirmation == "Manta y pañuelos"

    def test_fill_phone_number(self):
        self.routes_page.click_on_phone_number_button()
        self.routes_page.set_phone_number()
        self.routes_page.click_on_siguiente_button()
        self.routes_page.set_sms_code()
        self.routes_page.set_confirm_sms_code()
        phone_number = self.routes_page.get_click_on_phone_number_button()
        assert phone_number.text == data.phone_number

    def test_fill_payment_payment_method(self):
        self.routes_page.click_payment_method()
        self.routes_page.set_add_card_option()
        self.routes_page.set_card_number()
        self.routes_page.set_card_code()
        self.routes_page.get_card_code_field().send_keys(Keys.TAB)
        self.routes_page.set_card_submit_button()
        card = self.routes_page.get_card()
        assert card.text == 'Tarjeta'
        self.routes_page.set_payment_close_button()

    def test_message_for_driver(self):
        self.routes_page.set_message_for_driver_field()
        message = self.routes_page.get_message_for_driver_field()
        assert message.get_property('value') == data.message_for_driver

    def test_select_blanket_and_scarves(self):
        self.routes_page.set_blanket_and_scarves_option()
        assert self.routes_page.get_blanket_and_scarves_input().get_property("checked")

    def test_order_an_ice_cream(self):
        self.routes_page.set_ice_cream_button(2)
        assert self.routes_page.get_ice_cream_number().text == '2'

    def test_order_taxi_button(self):
        self.routes_page.set_order_taxi_button()
        assert "El conductor llegará en" in self.routes_page.get_request_confirmation().text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()