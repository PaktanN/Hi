from smartphone import Smartphone

# Создаем каталог из 5 смартфонов
catalog = [
    Smartphone("Apple", "iPhone 16", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79269876543"),
    Smartphone("Xiaomi", "Redmi Note 1", "+79001234567"),
    Smartphone("Huawei", "P40", "+79301234567"),
    Smartphone("Google", "Pixel 8", "+79401234567")
]

# Выводим весь каталог
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")