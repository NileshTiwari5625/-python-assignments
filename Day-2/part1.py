# 1. Cart Checkouts on Two Different Days
price_item_a = 100
price_item_b = 200
quantity_a_day1 = 2
quantity_b_day1 = 1
quantity_a_day2 = 4
quantity_b_day2 = 2

total_day1 = price_item_a * quantity_a_day1 + price_item_b * quantity_b_day1
total_day2 = price_item_a * quantity_a_day2 + price_item_b * quantity_b_day2

print(f"Day 1 Total: {total_day1}")
print(f"Day 2 Total: {total_day2}")
print(f"Is Day 2 total >= Day 1 total? {total_day2 >= total_day1}")

# 2. Shyam’s Square and Square Root Calculation
num_x = 5
num_y = 3
sum_xy = num_x + num_y

print(f"Sum: {sum_xy}")
print(f"Square of sum: {sum_xy ** 2}")
print(f"Square root of sum: {sum_xy ** 0.5}")

# 3. Zoya’s Discount Comparison
purchase_value = 4800

print(f"Is purchase >= 3000? {purchase_value >= 3000}")
print(f"Is purchase >= 5000? {purchase_value >= 5000}")

# 4. Laptop Surplus Check
total_laptops = 53
laptop_container_capacity = 8

containers_used = total_laptops / laptop_container_capacity
leftover_laptops = total_laptops % laptop_container_capacity

print(f"Containers filled: {containers_used}")
print(f"Leftover laptops: {leftover_laptops}")
print(f"Any leftover? {leftover_laptops != 0}")

# 5. Zaid’s Daily Expenses
daily_rent = 200
daily_food = 150

cost_3_days = 3 * (daily_rent + daily_food)
cost_5_days = 5 * (daily_rent + daily_food)

print(f"Cost for 3 days: {cost_3_days}")
print(f"Cost for 5 days: {cost_5_days}")
print(f"Is 5-day cost > 3-day cost? {cost_5_days > cost_3_days}")

# 6. Power Up: Manga Editor
scaling_factor = 4
triple_scaling = scaling_factor ** 3
double_scaling = scaling_factor ** 2

print(f"Triple scale: {triple_scaling}")
print(f"Double scale: {double_scaling}")
print(f"Is triple scale == 64? {triple_scaling == 64}")

# 7. Juice Bar Profit Check
price_orange_juice = 40
price_apple_juice = 60

monday_income = price_orange_juice * 10 + price_apple_juice * 5
tuesday_income = price_orange_juice * 8 + price_apple_juice * 7

print(f"Monday total: {monday_income}")
print(f"Tuesday total: {tuesday_income}")
print(f"Are totals different? {monday_income != tuesday_income}")

# 8. Tech Store: Adding & Removing Units
initial_laptop_stock = 45
final_laptop_stock = initial_laptop_stock + 10 - 3

print(f"Final stock: {final_laptop_stock}")
print(f"Is final stock > 50? {final_laptop_stock > 50}")

# 9. Mobile Plan Bill
call_cost_per_minute = 0.80
day1_call_minutes = 50
day2_call_minutes = 30

total_call_cost = call_cost_per_minute * (day1_call_minutes + day2_call_minutes)

print(f"Total Cost: {total_call_cost}")
print(f"Is total cost == 64.0 ? {total_call_cost == 64.0}")

# 10. Stringy Weight Lifting
weight_set1 = 60
weight_set2 = 70
total_weight_lifted = weight_set1 + weight_set2

print(f"Total Lifting: {total_weight_lifted} kg")
print(f"Is sum < 150? {total_weight_lifted < 150}")
