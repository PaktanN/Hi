import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, product_name):
        xpath = (f"//div[text()='{product_name}']/"
                 f"ancestor::div[@class='inventory_item']//button")
        add_button = (By.XPATH, xpath)
        self.driver.find_element(*add_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.cart_items))


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_input).send_keys(
            first_name)
        self.driver.find_element(*self.last_name_input).send_keys(
            last_name)
        self.driver.find_element(*self.zip_input).send_keys(zip_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def get_total(self):
        total_text = self.driver.find_element(*self.total_label).text
        return total_text


class TestSauceDemo:
    @pytest.fixture(scope="function")
    def setup(self):
        firefox_options = Options()
        firefox_options.add_argument("--start-maximized")
        service = Service()
        self.driver = webdriver.Firefox(
            service=service, options=firefox_options)
        self.driver.implicitly_wait(10)
        self.login_page = LoginPage(self.driver)
        yield
        self.driver.quit()

    def test_purchase_flow(self, setup):
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(self.driver)
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_to_cart("Sauce Labs Onesie")
        inventory_page.go_to_cart()

        cart_page = CartPage(self.driver)
        assert cart_page.get_cart_items_count() == 3
        cart_page.click_checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_info("Иван", "Иванов", "123456")
        checkout_page.click_continue()

        total = checkout_page.get_total()
        assert "58.29" in total, f"Expected $58.29, but got {total}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])