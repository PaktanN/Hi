from address import Address
from mailing import Mailing

# Создаем адрес отправки
to_addr = Address(
    index="12345",
    city="Москва",
    street="Ленина",
    house="10",
    apartment="15"
)

# Создаем адрес получения
from_addr = Address(
    index="11111",
    city="Санкт-Петербург",
    street="Невский",
    house="5",
    apartment="20"
)

# Создаем экземпляр Mailing
mailing = Mailing(to_address=to_addr, from_address=from_addr, cost=500, track="AB123456789RU")

# Вывод информации
print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} руб."
)