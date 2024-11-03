# Задача 1: Проверить, является ли число четным или нечетным
def check_even_odd(number):
    if number % 2 == 0:
        return f"Число {number} является четным."
    else:
        return f"Число {number} является нечетным."

print(check_even_odd(4))
