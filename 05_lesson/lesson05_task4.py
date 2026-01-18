from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    
    driver.find_element(By.ID, "username").send_keys("Dasha")
    driver.find_element(By.ID, "password").send_keys("123456789")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    flash_message = driver.find_element(By.ID, "flash").text
    print(flash_message)
    
finally:
    driver.quit()