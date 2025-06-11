# 1. Finding the Maximum and Minimum Values
def find_max_min(numbers):
    if not numbers:
        print("List is empty.")
        return

    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    print(f"Maximum value: {maximum}")
    print(f"Minimum value: {minimum}")

find_max_min([10, 5, 8, 12, 3])

# 2. Count Occurrences
def count_occurrences(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    print(f"{target} appears {count} times")

count_occurrences([1, 3, 7, 8, 3, 5, 3], 3)

# 3. Replace Negative Numbers with Zero
def replace_negatives_with_zero(numbers):
    updated_list = []
    for num in numbers:
        if num < 0:
            updated_list.append(0)
        else:
            updated_list.append(num)
    print(updated_list)

replace_negatives_with_zero([4, -3, 7, -1, 0, 5])

# 4. Reverse the List
def reverse_list(numbers):
    reversed_numbers = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_numbers.append(numbers[i])
    print(reversed_numbers)

reverse_list([1, 2, 3, 4, 5])

# 5. Concatenate two lists index-wise
def concatenate_lists_index_wise(list1, list2):
    concatenated_list = []
    for i in range(len(list1)):
        concatenated_list.append(list1[i] + list2[i])
    print(concatenated_list)

concatenate_lists_index_wise(["Hello", "Good"], ["World", "Morning"])

# 6. Turn every item of a list into its square
def square_list_elements(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num * num)
    print(squared_numbers)

square_list_elements([1, 2, 3, 4, 5])

# 7. Find common elements between two lists
def find_common_elements(list1, list2):
    common_elements = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in common_elements:
                common_elements.append(item1)
    print(common_elements)

find_common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])

# 8. Remove duplicates from a list
def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    print(unique_numbers)

remove_duplicates([1, 2, 3, 2, 4, 5, 3, 6, 5])

# 9. Calculate Total Price from Quantity and Prices
def calculate_total_price(quantities, prices):
    total_price = 0
    for i in range(len(quantities)):
        total_price += quantities[i] * prices[i]
    print(f"Total price = {total_price}")

calculate_total_price([2, 3, 5, 1], [50, 30, 20, 10])