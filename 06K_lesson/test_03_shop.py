import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shopping_cart_total(browser):
    browser.get("https://www.saucedemo.com/")
    
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    
    items = ["backpack", "bolt-t-shirt", "onesie"]
    for item in items:
        browser.find_element(By.ID, f"add-to-cart-sauce-labs-{item}").click()
    
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    browser.find_element(By.ID, "checkout").click()
    
    browser.find_element(By.ID, "first-name").send_keys("Test")
    browser.find_element(By.ID, "last-name").send_keys("User")
    browser.find_element(By.ID, "postal-code").send_keys("12345")
    browser.find_element(By.ID, "continue").click()
    
    total_element = browser.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    
    assert total_text == "Total: $58.29"