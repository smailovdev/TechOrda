# Задача 4: Проверить корректность введенной даты
from datetime import datetime

def check_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d.%m.%Y')
        return f"Дата {date_string} корректна."
    except ValueError:
        return f"Дата {date_string} некорректна."

print(check_valid_date("20.01.2002"))
