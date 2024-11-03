# Задача 7: Проверить, является ли число совершенным
def check_perfect_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    if divisors_sum == num:
        return f"Число {num} является совершенным."
    else:
        return f"Число {num} не является совершенным."

print(check_perfect_number(28))
