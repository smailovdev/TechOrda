# Задача 5: Найти совершенные числа в диапазоне от 0 до 1000
def find_perfect_numbers():
    perfect_numbers = []
    for num in range(1, 1001):
        divisors_sum = sum([i for i in range(1, num) if num % i == 0])
        if divisors_sum == num:
            perfect_numbers.append(num)
    return perfect_numbers

print(find_perfect_numbers())
