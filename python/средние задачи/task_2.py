# Задача 2: Проверить, является ли строка палиндромом
def check_palindrome(s):
    s = s.lower().replace(" ", "")
    if s == s[::-1]:
        return f"Строка '{s}' является палиндромом."
    else:
        return f"Строка '{s}' не является палиндромом."


print(check_palindrome("A man a plan a canal Panama"))
