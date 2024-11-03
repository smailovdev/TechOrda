# Задача 3: Проверить, является ли число простым
def check_prime(num):
    if num < 2:
        return f"Число {num} не является простым."
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return f"Число {num} не является простым."
    return f"Число {num} является простым."

print(check_prime(29))
