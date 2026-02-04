import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.driver.get(url)

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, button_text):
        if button_text == "+":
            locator = (By.XPATH, "//span[text()='+']")
        elif button_text == "-":
            locator = (By.XPATH, "//span[text()='−']")
        elif button_text == "*":
            locator = (By.XPATH, "//span[text()='×']")
        elif button_text == "/":
            locator = (By.XPATH, "//span[text()='÷']")
        elif button_text == "=":
            locator = (By.XPATH, "//span[text()='=']")
        else:
            locator = (By.XPATH, f"//span[text()='{button_text}']")

        self.driver.find_element(*locator).click()

    def get_result(self):
        def result_is_calculated(driver):
            screen = driver.find_element(*self.result_screen)
            text = screen.text
            if (text and text.strip()
                    and '+' not in text and '-' not in text
                    and '×' not in text and '÷' not in text):
                return text
            return False

        return self.wait.until(result_is_calculated)


class TestCalculator:
    @pytest.fixture(scope="function")
    def setup(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        service = Service()
        self.driver = webdriver.Chrome(
            service=service, options=chrome_options)
        self.driver.implicitly_wait(10)
        self.calculator_page = CalculatorPage(self.driver)
        yield
        self.driver.quit()

    def test_slow_calculator(self, setup):
        self.calculator_page.open()
        self.calculator_page.set_delay(45)

        self.calculator_page.click_button("7")
        self.calculator_page.click_button("+")
        self.calculator_page.click_button("8")
        self.calculator_page.click_button("=")

        result = self.calculator_page.get_result()
        assert result == "15", f"Expected '15', but got '{result}'"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])