# Задача 6: Проверить, является ли число числом Фибоначчи
def is_fibonacci_number(n):
    def is_perfect_square(x):
        s = int(x ** 0.5)
        return s * s == x
    
    if is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4):
        return f"Число {n} является числом Фибоначчи."
    else:
        return f"Число {n} не является числом Фибоначчи."

print(is_fibonacci_number(25))
