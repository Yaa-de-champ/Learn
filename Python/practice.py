# def display_cash():
#     money = 100
#     currency = "Euros"
#     print(f"{money} Euros")
# display_cash()
#
# def add_ten_to(number):
#     print(number+10)
# add_ten_to(15)
#
# def make_greeting(name):
#     print(f"Hi there, {name}")
# make_greeting("Tom")
#
# def get_brightness():
#     brightness = 67
#     return brightness
# print(get_brightness())
from fontTools.misc.cython import returns

# def sign_up(user):
#     status = user + "signed up"
#     return status
# print(sign_up("Jo"))
#
# def get_area(height):
#     width = 26;
#     return width + height
# print(f"Rectangle area: {get_area(100)}")
#
# def get_total(item1, item2, item3):
#     total = item1 + item2 + item3
#     return total
# cart = get_total(5.5, 8, 50)
# print(cart)


# def display_instructions(add_sugar):
#     if add_sugar:
#         print("Enter amount of sugar")
#     print("Select coffee type")
# display_instructions(False)
#
# def has_red(rgb_values):
#     if rgb_values[0] > 0:
#         print("Red is in the mix!")
# rgb = [153, 255, 51]
# has_red(rgb)
#
# def add_sports(plans):
#     plans[0] = "Jogging"
# plans=["reading", "cooking", "shopping with girls"]
# add_sports(plans)
# print(plans)
#
# def is_valid(parts):
#     print(len(parts) == 2)
# email = "dokuamponsah@gmail.com"
# user_and_domain = email.split("@")
# is_valid(user_and_domain)
#
# def onboard_passengers(bookings):
#     counter = 0
#     while counter <= bookings:
#         counter += 1
#     print("Onboarding passenger")
# onboard_passengers(4)
#
# def help_customers(customers):
#     counter = 1
#     while counter < customers:
#         print(f"Customer no.{counter} go to the next free desk")
#         counter += 1
# help_customers(3)
#
# def show_instructions(ingredients):
#     for item in ingredients:
#         print(f"Stir in: {item}")
# cake = ["flour", "softened butter", "milk", "sugar", "eggs"]
# hot_chocolate = ["milk", "chocolate"]
# show_instructions(hot_chocolate)
#
# def show_notifications(messages):
#     for i in range(messages):
#         print("Failed to send message")
# show_notifications(3)


# # FOOD ORDER SYSTEM PROJECT
# italian_food = ["Pasta Bolognese",
#                 "Pepperoni pizza",
#                 "Margherita pizza",
#                 "Lasagna"]
#
# indian_food = ["Curry",
#                "Chutney",
#                "Samosa",
#                "Naan" ]
#
# def find_meal(name, menu):
#     return name if name in menu else None
#
#
# def select_meal(name, food_type):
#         if food_type == "Italian":
#             return find_meal(name, italian_food)
#         elif food_type == "Indian":
#             return find_meal(name, indian_food)
#         else:
#             return None
#
#
# def display_available_meals(food_type):
#     if food_type == "Italian":
#         print("Available Italian Meals:")
#         for meal in italian_food:
#             print(meal)
#     elif food_type == "Indian":
#         print("Available Indian Meals:")
#         for meal in indian_food:
#             print(meal)
#     else:
#         print("Invalid food type")
#
#
# def create_summary(name, amount, food_type):
#     order = select_meal(name, food_type)
#     if order:
#         return f"You ordered {amount} piece(s) of {name} "
#     else:
#         return "Meal not found"
#
# print("Welcome to the Food Order System!")
#
# type_input = input(" Choose type(Italian Food or Indian Food): ")
# display_available_meals(type_input)
#
# name_input = input("Enter the name of the meal you want to order: ")
# amount_input = int(input("Enter the quantity you want to order: "))
#
# result = create_summary(name_input, amount_input, type_input)
# print(result)
#


# shopping_list = ['apples','chips','eggs','chocolate']
# for item in shopping_list:
#     if item == 'chips':
#         continue
#     print(f"Don't forget to buy some {item}")
#
# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

# password = "open_sesame"
# while True:
#     if input("Enter the password: ") == password:
#         print("Access granted!")
#         break
#     print("Incorrect password. Try again.")
#
# tasks = ['pending', 'completed', 'pending']
# index = 0
# while index < len(tasks):
#     if tasks[index] == "completed":
#         print(f"skipping task {index + 1}")
#         index += 1
#         continue
#     print(f"processing task {index + 1}")
#     index += 1
#
# from time import sleep
# print("Hey thereeee")
# sleep(5)
# print("Hi")

# total = 5
# people = 10
# try:
#     share = total/people
# except:
#     pass
# else:
#     print("Your share is " + str(share)+ " units.")
#
#
# users = ['John', 'Ellie', 'Rachel']
# user = 'John'
# try:
#     users.index(user)
#     print("Welcome back, " + user)
# except:
#     print("Do you want to become a member?")
# finally:
#     print("See our web site for offers for both member and non-member")