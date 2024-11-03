# Задача 8: Определить сезон года по введенной дате
def get_season(date_string):
    day, month = map(int, date_string.split('.'))
    
    if (month == 12 and day >= 21) or (1 <= month <= 2) or (month == 3 and day <= 20):
        return "Зима"
    elif (month == 3 and day >= 21) or (4 <= month <= 5) or (month == 6 and day <= 20):
        return "Весна"
    elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day <= 22):
        return "Лето"
    else:
        return "Осень"

print(get_season("15.10"))
