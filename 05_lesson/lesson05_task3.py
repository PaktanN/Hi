import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():

    driver = webdriver.Firefox()
    
    try:

        driver.get("http://the-internet.herokuapp.com/inputs")
        time.sleep(1)
        
        input_field = driver.find_element(By.TAG_NAME, "input")
        
        input_field.send_keys("Sky")
        print("Введен текст: Sky")
        time.sleep(1)
        
        input_field.clear()
        time.sleep(1)

        input_field.send_keys("Pro")
        time.sleep(2)
        
    finally:
        driver.quit()
