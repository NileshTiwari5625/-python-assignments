# Question 1: Print a Greeting
def print_hello():
    print("Hello, World!")

print_hello()

# Question 2: Personalized Greeting
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Question 3: Add Two Numbers
def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(5, 7)

# Question 4: Return Sum
def add_numbers_return_sum(num1, num2):
    return num1 + num2

result = add_numbers_return_sum(5, 7)
print(result)

# Question 5: Check Even or Odd
def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(5))

# Question 6: Print Even Numbers
def print_even_numbers():
    for i in range(1, 21):
        if is_even(i):
            print(i)

print_even_numbers()

# Question 7: Calculate Circle Area
def calculate_area(radius):
    pi = 3.14
    return pi * (radius ** 2)

area = calculate_area(5)
print(area)

# Question 8: Fibonacci Number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

print(fibonacci(5))

# Question 9: Factorial Calculation
def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

print(factorial(5))

# Question 10: Check Prime Number
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(8))

# Question 11: Print Prime Numbers
def print_prime_numbers_up_to_50():
    for i in range(1, 51):
        if is_prime(i):
            print(i)

print_prime_numbers_up_to_50()

# Question 12: Reverse a String
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

print(reverse_string("hello"))

# Question 13: Check Palindrome
def is_palindrome(s):
    # Convert to lowercase and remove spaces for a more robust check if needed
    # s = s.lower().replace(" ", "")
    return s == reverse_string(s)

print(is_palindrome("racecar"))
print(is_palindrome("python"))

# Question 14: Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello"))

# Question 15: Find Maximum Number
def maximum(num1, num2, num3):
    max_val = num1
    if num2 > max_val:
        max_val = num2
    if num3 > max_val:
        max_val = num3
    return max_val

print(maximum(10, 20, 15))

# Question 16: Sum of List
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_of_list([1, 2, 3, 4]))

# Question 17: Multiply List Elements
def multiply_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

print(multiply_list([1, 2, 3, 4]))

# Question 18: Multiplication Table
def generate_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

generate_multiplication_table(5)

# Question 19: Calculate Grade
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print(calculate_grade(85))

# Question 20: Remove Duplicates from List
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

print(remove_duplicates([1, 2, 3, 2, 4, 5, 3, 6, 5]))