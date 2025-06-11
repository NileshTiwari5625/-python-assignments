# Problem 1: Highest Scoring Student
def highest_scoring_student(student_scores):
    highest_score = -1
    highest_scorer = ""
    for student, score in student_scores.items():
        if score > highest_score:
            highest_score = score
            highest_scorer = student
    print(f"{highest_scorer} {highest_score}")

student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 88,
    "Diana": 95
}
highest_scoring_student(student_scores)

# Problem 2: Total Shopping Cart Price
def total_shopping_cart_price(shopping_cart):
    total_price = 0.0
    for price in shopping_cart.values():
        total_price += price
    print(f"Total price: {total_price}")

shopping_cart = {
    "apple": 2.5,
    "banana": 1.2,
    "milk": 3.0,
    "bread": 2.0
}
total_shopping_cart_price(shopping_cart)

# Problem 3: Country Capitals
def country_capitals_lookup(countries, capitals):
    country_capital_map = dict(zip(countries, capitals))
    user_input = input("Enter country name: ")
    if user_input in country_capital_map:
        print(f"The capital of {user_input} is {country_capital_map[user_input]}.")
    else:
        print(f"Capital for {user_input} not found.")

countries = ["India", "France", "Japan", "Canada"]
capitals = ["New Delhi", "Paris", "Tokyo", "Ottawa"]
# Uncomment the line below to run the interactive part
# country_capitals_lookup(countries, capitals)

# For automated testing, let's simulate the input:
print("\n--- Simulating Country Capitals Lookup for 'Japan' ---")
country_capital_map_simulated = dict(zip(countries, capitals))
simulated_input = "Japan"
if simulated_input in country_capital_map_simulated:
    print(f"The capital of {simulated_input} is {country_capital_map_simulated[simulated_input]}.")
else:
    print(f"Capital for {simulated_input} not found.")
print("--- End of simulation ---\n")


# Problem 4: Filter Dictionary by Value
def filter_dictionary_by_value(numbers_dict, threshold):
    filtered_dict = {}
    for key, value in numbers_dict.items():
        if value <= threshold:
            filtered_dict[key] = value
    print(filtered_dict)

numbers = {
    "a": 10,
    "b": 15,
    "c": 5,
    "d": 20
}
threshold = 12
filter_dictionary_by_value(numbers, threshold)

# Problem 5: Merge Dictionaries
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy() # Start with a copy of dict1
    merged_dict.update(dict2)   # Update with dict2 (overwrites duplicates)
    print(merged_dict)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'd': 4}
merge_dictionaries(dict1, dict2)

# Problem 6: Employee Departments
def print_employee_departments(employees_dict):
    for emp_id, details in employees_dict.items():
        print(f"{details['name']} works in {details['department']} department.")

employees = {
    "emp1": {"name": "John", "department": "HR"},
    "emp2": {"name": "Emma", "department": "IT"},
    "emp3": {"name": "Harry", "department": "Finance"}
}
print_employee_departments(employees)

# Problem 7: Word Frequency Counter
def word_frequency_counter(sentence):
    words = sentence.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    print(word_counts)

sentence = "hello world hello"
word_frequency_counter(sentence)

# Problem 8: Clean Inventory
def clean_inventory(inventory_dict):
    cleaned_inventory = {}
    for item, quantity in inventory_dict.items():
        if quantity > 0:
            cleaned_inventory[item] = quantity
    print(cleaned_inventory)

inventory = {
    "pen": 10,
    "pencil": 0,
    "eraser": 5,
    "notebook": 0
}
clean_inventory(inventory)

# Problem 9: Number Squares Dictionary
def number_squares_dictionary(n):
    squares_dict = {}
    for i in range(1, n + 1):
        squares_dict[i] = i * i
    print(squares_dict)

number_squares_dictionary(5)

# Problem 10: Add Subject to Students
def add_subject_to_students(students_dict, new_subject):
    for student, subjects in students_dict.items():
        subjects.append(new_subject)
    print(students_dict)

students = {
    "Alice": ["Math", "Science"],
    "Bob": ["English"],
    "Charlie": ["History", "Math"]
}
new_subject = "Physical Education"
add_subject_to_students(students, new_subject)

# Problem 11: Find Common Keys
def find_common_keys(dict1, dict2):
    common_keys = []
    for key in dict1:
        if key in dict2:
            common_keys.append(key)
    print(f"Common keys: {common_keys}")

dict1 = {'x': 1, 'y': 2, 'z': 3}
dict2 = {'w': 10, 'x': 11, 'y': 22}
find_common_keys(dict1, dict2)

# Problem 12: Invert a Dictionary
def invert_dictionary(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        inverted_dict[value] = key
    print(inverted_dict)

original_dict = {'a': 1, 'b': 2, 'c': 3}
invert_dictionary(original_dict)

# Problem 13: Convert List of Tuples to Dictionary
def convert_list_of_tuples_to_dict(list_of_tuples):
    result_dict = dict(list_of_tuples)
    print(result_dict)

list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
convert_list_of_tuples_to_dict(list_of_tuples)

# Problem 14: Character Frequency in String
def character_frequency(input_string):
    char_freq = {}
    for char in input_string:
        char_freq[char] = char_freq.get(char, 0) + 1
    print(char_freq)

input_string = "mississippi"
character_frequency(input_string)

# Problem 15: Word Length Mapping
def word_length_mapping(words_list):
    length_map = {}
    for word in words_list:
        length_map[word] = len(word)
    print(length_map)

words = ["apple", "banana", "cherry"]
word_length_mapping(words)