import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestForm:
    """Тест для проверки формы с валидацией полей"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Настройка перед каждым тестом"""
        # Используем Edge браузер
        self.driver = webdriver.Edge()
        self.wait = WebDriverWait(self.driver, 10)
        
        yield
        
        self.driver.quit()
    
    def test_form_validation(self):
        """Тест заполнения формы и проверки валидации"""
        
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
        self._fill_form()
        
        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()
        
        zip_code_field = self.driver.find_element(By.ID, "zip-code")
        zip_code_classes = zip_code_field.get_attribute("class")
        
        assert "is-invalid" in zip_code_classes, \
            "Поле Zip code должно быть подсвечено красным"
        
        green_fields = [
            ("first-name", "First name"),
            ("last-name", "Last name"),
            ("address", "Address"),
            ("e-mail", "Email"),
            ("phone", "Phone number"),
            ("city", "City"),
            ("country", "Country"),
            ("job-position", "Job position"),
            ("company", "Company")
        ]
        
        for field_id, field_name in green_fields:
            field = self.driver.find_element(By.ID, field_id)
            field_classes = field.get_attribute("class")
            
            assert "is-valid" in field_classes, \
                f"Поле {field_name} должно быть подсвечено зеленым"
    
    def _fill_form(self):
        """Вспомогательный метод для заполнения формы"""
        form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            # "zip-code": "" оставляем пустым
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }
        
        for field_id, value in form_data.items():
            field = self.wait.until(
                EC.presence_of_element_located((By.ID, field_id))
            )
            field.clear()
            field.send_keys(value)