def is_year_leap(year):
    return year % 4 == 0
# Проверка функции is_year_leap


year = 2026 
result = is_year_leap(year)

print(f"год {year}: {result}")