import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def click_dynamic_button():
    
    driver = webdriver.Chrome()
    
    try:
        driver.get("http://uitestingplayground.com/dynamicid")
        time.sleep(1)
        
        button = driver.find_element(By.XPATH, 
                                     "//button[text()='Button with Dynamic ID']")
        
        print(f"Найдена кнопка: '{button.text}'")
        print(f"Динамический ID: {button.get_attribute('id')}")
        
        button.click()
        print("Клик выполнен успешно!")
        
        time.sleep(2)
        
    finally:
        driver.quit()