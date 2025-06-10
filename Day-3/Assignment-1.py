#1.Movie Ticket Age Check

age = int(input("Enter the child's age: "))

if age < 5:
    print("Free Ticket!")

#2. Speed Monitoring

speed = int(input("Enter speed in kmph:"))

if speed > 100:
    print("Overspeeding! Slow down!")
else:
    print("Speed is okay.")

#3. Travel Mode Selector

mode = input("Enter mode of travel (walk, bus, car): ")

if mode == "walk":
    print("Cost = 0")
elif mode == "bus":
    print("Cost = 10")
else:
    print("Cost = 50")

#4. Nested Student Access
  

user_type = input("Enter user type: ")
student_card = input("Do you have a student card? (yes/no): ") == "yes"

if user_type == "student":
    if student_card:
        print("Access to Student Portal")
    else:
        print("No Access")
else:
    print("No Access")


#5.AND Condition for Admission

tenth_marksheet = input("Enter the marksheet:")
id_proof = input("Enter the id_proof")\

if (tenth_marksheet == True and id_proof == True):
    print("Admission possible")
else:
    print("Admission Blocked")
    
#6. OR Condition for Concert Entry

VIP_pass = input("Upload the Vip pass")
staff_Badge = input("Upload the badge")

if VIP_pass or staff_Badge:
    print("Enjoy the Concert")
else:
    print("Ticket needed")

#7.Combined Condition for Clubbing



while True:
    try:
        age_input = input("Please enter your age: ")
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative. Please try again.")
        else:
            break 
    except ValueError:
        print("Invalid input. Please enter a number for your age.")


while True:
    gender_input = input("Are you male or female? (Type 'male' or 'female'): ").lower()
    if gender_input == 'male':
        male = True
        female = False
        break
    elif gender_input == 'female':
        male = False
        female = True
        break
    else:
        print("Invalid input. Please type 'male' or 'female'.")

if (age >= 21) and (male or female):
    print("Entry granted")
else:
    print("Entry denied")

#8. Nested If for Purchase Discount

is_member = bool(input("Enter:"))
bill_amount = int(input("Enter:"))
if is_member == True:
    if bill_amount >= 1000:
        print("Gold Discount")
    else:
        print("Regular Discount")
else:
    print("No discount")

#9. Food Order Preference 


meal_choice = input("What would you like to order? (pizza, pasta, or burger): ").lower()


if meal_choice == "pizza" or meal_choice == "pasta":
    print("Italian Meal")
elif meal_choice == "burger":
    print("American Meal")
else:
    print("No meal found.")

#10. Nested Family Access Example

family_input = input("Are you a family member? (yes/no): ").lower()
family_member = (family_input == "yes")

invitation_card = False
if family_member:
    card_input = input("Do you have an invitation card? (yes/no): ").lower()
    invitation_card = (card_input == "yes")

if family_member:
    if invitation_card:
        print("Welcome, cousin!")
    else:
        print("Get your card from the reception.")
else:
    print("Stranger not allowed!")

