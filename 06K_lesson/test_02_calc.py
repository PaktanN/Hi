import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(browser):
    wait = WebDriverWait(browser, 50)
    
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    
    buttons = ["7", "+", "8", "="]
    
    for button_text in buttons:
        button = browser.find_element(
            By.XPATH,
            f"//span[text()='{button_text}']"
        )
        button.click()
    
    screen = browser.find_element(By.CLASS_NAME, "screen")
    
    wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    
    final_result = screen.text
    assert final_result == "15", f"Expected '15', got '{final_result}'"