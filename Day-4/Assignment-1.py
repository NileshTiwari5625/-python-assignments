john_position = 0
iteration_count = 0
goal = 100

while john_position < goal:
    iteration_count += 1

    # John advances 4 meters
    john_position += 4
    print(f"John at {john_position} meters")

    # Apply rest logic
    if iteration_count % 2 == 0:
        john_position -= 1 # He rests, moving back 1 meter
        print(f"John at {john_position} meters (after rest)")
    
    # Check if goal is reached (specifically when he lands on 100)
    if john_position >= goal:
        print("John at 100 meters (Goal Reached)")
        break # Exit the loop once the goal is reached



def smartwatch_steps_tracker():
    goal_steps = 10000
    alert_interval = 2000
    current_steps = 0
    next_alert_steps = alert_interval

    print("Smartwatch Steps Tracker Started!")
    print(f"Goal: {goal_steps} steps")

    while current_steps < goal_steps:
        steps_taken_in_interval = int(input(f"Enter steps taken (current: {current_steps} / {goal_steps}): "))

        if steps_taken_in_interval <= 0:
            print("Please enter a positive number of steps.")
            continue

        current_steps += steps_taken_in_interval

        while current_steps >= next_alert_steps and next_alert_steps <= goal_steps:
            print(f"--- ALERT! You've reached {next_alert_steps} steps! Keep going! ---")
            next_alert_steps += alert_interval

        if next_alert_steps > goal_steps and current_steps < goal_steps:
            next_alert_steps = goal_steps

        print(f"Current steps: {current_steps}")

    print(f"\n--- CONGRATULATIONS! You've reached your daily goal of {goal_steps} steps! ---")
    print("Great job!")

#2. Smartwatch Steps Tracker

import math

def smartwatch_steps_tracker():
    goal_steps = 10000
    alert_interval = 2000
    current_steps = 0
    next_alert_steps = alert_interval

    print("Smartwatch Steps Tracker Started!")
    print(f"Goal: {goal_steps} steps")

    while current_steps < goal_steps:
        steps_taken_in_interval = int(input(f"Enter steps taken (current: {current_steps} / {goal_steps}): "))

        if steps_taken_in_interval <= 0:
            print("Please enter a positive number of steps.")
            continue

        current_steps += steps_taken_in_interval

        while current_steps >= next_alert_steps and next_alert_steps <= goal_steps:
            print(f"--- ALERT! You've reached {next_alert_steps} steps! Keep going! ---")
            next_alert_steps += alert_interval

        if next_alert_steps > goal_steps and current_steps < goal_steps:
            next_alert_steps = goal_steps

        print(f"Current steps: {current_steps}")

    print(f"\n--- CONGRATULATIONS! You've reached your daily goal of {goal_steps} steps! ---")
    print("Great job!")

smartwatch_steps_tracker()


#3. countdown to a new year
import time

def new_year_countdown():
    countdown_start = 10

    while countdown_start > 0:
        print(countdown_start)
        time.sleep(1)
        countdown_start -= 1
    
    print("Happy New Year!")

new_year_countdown()

#4. Ice Cream Sales Counter

def ice_cream_sales():
    stock = 50
    customer_count = 0
    
    while stock >= 3:
        customer_count += 1
        stock -= 3
        print(f"Customer {customer_count} served, Ice creams left: {stock}")
    
    print(f"No more ice creams! Customers served: {customer_count}")

ice_cream_sales()

#5. Store Discounts Based on Shopping Amount
def store_discounts():
    customer_amounts = [700, 4500, 1200]

    for i, amount in enumerate(customer_amounts):
        discount_percentage = 0
        if amount > 5000:
            discount_percentage = 30
        elif amount > 1000:
            discount_percentage = 20
        elif amount > 500:
            discount_percentage = 10
        
        if discount_percentage > 0:
            print(f"Customer {i+1} gets {discount_percentage}% discount.")
        else:
            print(f"Customer {i+1} gets no discount.")

store_discounts()

#6.Even & Odd Race
def even_odd_race():
    for runner_number in range(1, 21):
        if runner_number % 2 == 0:
            print(f"Runner {runner_number} → Team Blue")
        else:
            print(f"Runner {runner_number} → Team Red")

even_odd_race()

#7.Generate a Multiplication Table
def multiplication_table():
    try:
        number = int(input("Enter a number: "))
        for i in range(1, 11):
            print(f"{number} × {i} = {number * i}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

multiplication_table()

#8.Finding the First Number Divisible by Both 7 and 5
def find_first_divisible():
    found_number = None
    for num in range(1, 101):
        if num % 7 == 0 and num % 5 == 0:
            found_number = num
            break
    
    if found_number is not None:
        print(f"The first number divisible by both 7 and 5 between 1 and 100 is: {found_number}")
    else:
        print("No such number found between 1 and 100.")

find_first_divisible()

#9. Sum of Even Numbers Between 1 and 200

def sum_of_even_numbers():
    total_sum = 0
    for num in range(2, 201, 2):
        total_sum += num
    
    print(f"Sum of even numbers between 1 and 200: {total_sum}")

sum_of_even_numbers()

#10.Find How Many Digits Are in a Given Number

def count_digits():
    try:
        number_str = input("Enter a number: ")
        
        if not number_str.strip():
            print("Number of digits: 0")
            return

        num = int(number_str)
        
        if num == 0:
            print("Number of digits: 1")
            return

        count = 0
        temp_num = abs(num) 
        
        while temp_num > 0:
            temp_num //= 10
            count += 1
        
        print(f"Number of digits: {count}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

count_digits()

#11. Reverse Counting for a Rocket Launch

import time

def rocket_countdown():
    for i in range(20, -1, -1):
        if i == 5:
            print(f"{i}: Conducting final safety check...")
            time.sleep(2)
        else:
            print(i)
        time.sleep(1)
    
    print("Liftoff! We have ignition!")

rocket_countdown()