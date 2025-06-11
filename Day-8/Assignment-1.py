# Q1. Print Characters at Even Indexes
def print_even_index_chars(input_string):
    result = ""
    for i in range(len(input_string)):
        if i % 2 == 0:
            result += input_string[i]
    print(result)

print_even_index_chars("Laptop")

# Q2. Append a Character and Print
def append_char(input_string, char_to_append):
    print(input_string + char_to_append)

append_char("GoodDay", "#")

# Q3. Print String in Reverse (Using Loop Only)
def reverse_string_loop(input_string):
    reversed_str = ""
    for i in range(len(input_string) - 1, -1, -1):
        reversed_str += input_string[i]
    print(reversed_str)

reverse_string_loop("Galaxy")

# Q4. Count Lowercase Letters
def count_lowercase_letters(input_string):
    count = 0
    for char in input_string:
        if 'a' <= char <= 'z':
            count += 1
    print(count)

count_lowercase_letters("WiFiRouter")

# Q5. Replace All 'e' With '*'
def replace_e_with_star(input_string):
    result = ""
    for char in input_string:
        if char == 'e':
            result += '*'
        else:
            result += char
    print(result)

replace_e_with_star("Greenhouse")

# Q6. Count Words in a Sentence
def count_words_in_sentence(sentence):
    words = 0
    in_word = False
    for char in sentence:
        if char == ' ':
            in_word = False
        elif not in_word:
            words += 1
            in_word = True
    print(words)

count_words_in_sentence("Coding is really fun sometimes")

# Q7. Remove All Vowels From the String
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    print(result)

remove_vowels("Adventure")

# Q8. Join Characters Using & Symbol
def join_with_ampersand(input_string):
    result = ""
    for i in range(len(input_string)):
        result += input_string[i]
        if i < len(input_string) - 1:
            result += "&"
    print(result)

join_with_ampersand("world")

# Q9. Count Strings That Contain 'e' in a List
def count_strings_with_e(string_list):
    count = 0
    for s in string_list:
        if 'e' in s or 'E' in s:
            count += 1
    print(count)

count_strings_with_e(["Pine", "Oak", "Maple", "Neem", "Banyan"])

# Q10. Password Strength Checker
def check_password_strength(password):
    if len(password) <= 6:
        print("Weak Password")
    else:
        has_digit = False
        for char in password:
            if '0' <= char <= '9':
                has_digit = True
                break
        if has_digit:
            print("Strong Password")
        else:
            print("Medium Password")

check_password_strength("hello123")

# Q11. Remove All Digits from the String
def remove_digits_from_string(input_string):
    result = ""
    for char in input_string:
        if not ('0' <= char <= '9'):
            result += char
    print(result)

remove_digits_from_string("my id is 508L00")