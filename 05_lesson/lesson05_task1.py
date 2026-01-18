import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def click_blue_button():
    """Запускает браузер, переходит на страницу и кликает синюю кнопку."""
    
    # Инициализируем драйвер Chrome
    driver = webdriver.Chrome()
    
    try:
  
        print("Переходим на страницу...")
        driver.get("http://uitestingplayground.com/classattr")

        blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        
        print("Кликаем на синюю кнопку...")
        blue_button.click()
        
        time.sleep(1)  
        alert = driver.switch_to.alert
        print(f"Текст всплывающего окна: {alert.text}")
        alert.accept()
        
        time.sleep(1)
        
        print("Успешно! Синяя кнопка была нажата.")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        
    finally:
        print("Закрываем браузер...")
        driver.quit()
