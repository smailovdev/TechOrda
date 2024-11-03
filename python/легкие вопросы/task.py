# int-cmp
def int_cmp(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

# max-of-three
def max_of_three(a, b, c):
    return max(a, b, c)

# sqr-sum-1-n
def sqr_sum_1_n(n):
    return sum(i ** 2 for i in range(1, n + 1))

# print-even-a-b
def print_even_a_b(a, b):
    return [i for i in range(a, b + 1) if i % 2 == 0]

# pow-a-b
def pow_a_b(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

# calc-deposit
def calc_deposit(n, k, b):
    return b * ((1 + k / 100) ** n)

# min
def min_in_array(array):
    return min(array) if array else 0

# range
def range_n(n):
    return list(range(1, n + 1))

# sum
def sum_of_array(array):
    return sum(array)

# sort (bubble)
def sort_array(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print(int_cmp(1, 0))                
print(max_of_three(42, 1, 0))       
print(sqr_sum_1_n(3))               
print(print_even_a_b(0, 4))         
print(pow_a_b(2, 6))                
print(calc_deposit(1, 5, 1000))     
print(min_in_array([1, 2, 3]))      
print(range_n(5))                   
print(sum_of_array([1, 2, 3]))      
print(sort_array([3, 2, 1]))        
