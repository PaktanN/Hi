from string_utils import StringUtils

# Создаем экземпляр утилит

utils = StringUtils()

# Тесты для метода capitalize


def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello") == "Hello"
    assert utils.capitalize("123") == "123"
    assert utils.capitalize("  test") == "  test"  
    # Первый символ пробел, ничего не поменяет
    assert utils.capitalize("") == ""


def test_capitalize_negative():
    assert utils.capitalize(None) == ""
    assert utils.capitalize(123) == ""
    assert utils.capitalize(["list"]) == ""


# Тесты для метода trim

def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("     test string") == "test string"
    assert utils.trim("noLeadingSpace") == "noLeadingSpace"
    assert utils.trim(" ") == ""
    assert utils.trim("") == ""


def test_trim_negative():
    assert utils.trim(None) == ""
    assert utils.trim(123) == ""
    assert utils.trim(["list"]) == ""


# Тесты для метода contains

def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "k") is True
    assert utils.contains("SkyPro", "P") is True
    assert utils.contains("SkyPro", "o") is True
    assert utils.contains("Тест", "Т") is True


def test_contains_negative():
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("SkyPro", "z") is False
    assert utils.contains("", "a") is False
    assert utils.contains(None, "a") is False
    assert utils.contains("SkyPro", None) is False
    assert utils.contains(12345, "1") is False


# Тесты для метода delete_symbol

def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyProPro", "Pro") == "Sky"
    assert utils.delete_symbol("aaaaaa", "a") == ""
    assert utils.delete_symbol("123-456-789", "-") == "123456789"
    

def test_delete_symbol_negative():
    assert utils.delete_symbol(None, "a") == ""
    assert utils.delete_symbol("SkyPro", None) == ""
    assert utils.delete_symbol("", "a") == ""
    assert utils.delete_symbol("Test", "") == "Test"  

# Удаление пустой строки не меняет