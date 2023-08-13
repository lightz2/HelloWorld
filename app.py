# Variable tutorial
# name = "John Smith"
# age = 20
# is_new = True

# input tutorial
# name = input("What is your name? ")
# print("Hi " + name)

# exercise
# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# print(name + " likes " + color)

# type converstion
# birth_year = input("Birth year: ")
# print(type(birth_year))
# age = 2023 - int(birth_year)
# print(type(age))
# print(age)

# exercise
# weight = input("weight (lbs): ")
# kilogram = float(weight) * 0.453
# print(kilogram)

# strings

# ex:1
# course = "Python's Course for Beginners"
# print(course)

# ex:2
# course = """
# Hi john,

# Here is our first email to you.

# Thank you,
# The support team.
# """
# print(course)

# ex:3 
# course = "Python for Beginners"
# print(course[0])
# ex:4
# print(course[0:3])
# print(course[:])

# name = "Jennifer"
# print(name[1:-1])

# formatted Sting tutorial
# first = "John"
# last = "Smith"
# message = first + " [" + last + "] is a coder"
# msg = f"{first} [{last}] is a coder"
# print(msg)

# string method
# course = "Python for Beginners"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find("p"))
# print(course.replace("Beginners", "Absolute Beginners"))
# print("Python" in course)

# Arithemetic Operations tutorial
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# ex:1
# x = 10
# x += 3
# print(x)

# Operator precedence
# x = (10 + 3) * 2 ** 2
# print(x)

# the order
# parenthesis
# exponentiation 2**3
# multiplication or division
# addition or subtraction

# exercise
# x = (2 + 3) * 10 - 3
# print(x)

# math funtion
# import math
# x = 2.9
# print(round(x))
# print(abs(-2.9))
# print(math.ceil(2.9))
# print(math.floor(x))

# if statement tutorial
# is_hot = False
# is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("Its a cold day")
#     print("Wear warm clothes") 
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

# exercise
# price_of_house = 1000000
# has_good_credit = False

# if has_good_credit:
#     down_payment = 0.1 * price_of_house
# else:
#     down_payment = 0.2 * price_of_house
# print(f"down_payment: {down_payment}")

# logical operators
# has_high_income = False
# has_good_credit = True

# if has_high_income and has_good_credit:
#     print("Eligible for loan")

# if has_high_income or has_good_credit:
#     print("Eligible for loan")

# AND: both
# OR: at least one
# NOT: 

# comparison operator
# >: greater than
# <: less than
# ==: equal to
# >=: greater than or equal to
# <=: less than or equal to
# !=: not equal to
# temperature = 35

# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

# exercise
# name = input("Name: ")
# len_name = len(name)

# if len_name < 3:
#     print("Name must be at least 3 characters")
# elif len_name > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good!")

# while loop tutorial
# ex:1
# i = 1
# while i <= 5:
#     print("*" * i)
#     i = i + 1
# print("Done")

# for loop tutorial
# ex:1
# for item in "python":
#     print(item)
# ex:2
# for item in ["senator", "mosh", "amen"]:
    # print(item)
# ex:3
# for item in [1, 2, 3, 4, 5]:
#     print(item)
# ex:4
# for item in range(5, 10, 2):
#     print(item)

# exercise
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")

# nested loop tutorial
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

# exercise
# number = [2, 2, 2, 2, 5]
# for x_co in number:
#     output = ""
#     for count in range(x_co):
#         output += "x"
#     print(output)

# lists tutorial 
# name = ["John", "Senator", "Mosh", "Dammy"]
# print(len(name))

# exercise
# numbers = [3, 4, 2, 5, 1, 7, 10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# 2d lists tutorial i.e two dimentional lists
# matrix = [
#     [1, 2, 3],
#     [4 ,5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][1])

# matrix = [
#     [1, 2, 3],
#     [4 ,5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)

# list methods tutorial
# numbers = [5, 2, 1, 5, 7, 4]
# numbers.append(20)
# numbers.insert(0, 10)
# numbers.remove(2)
# numbers.clear()
# numbers.pop()
# print(numbers.index(5))
# print(15 in numbers)
# print(numbers.count(5))
# print(numbers.sort())
# numbers2 = numbers.copy()
# print(numbers)

# exercise
# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# tuples tutorial
# numbers = (1, 2, 3, 4)
# print(numbers[0])

# unpacking tutorial
# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(x)

# dictionaries tutorial
# customer = {
#     "name": "john smith",
#     "age": 30,
#     "is_varified": True
# }
# customer["name"] = "senator smith"
# print(customer["name"])
# print(customer.get("birthday"))

# phone = input("Phone: ")
# digit_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = " "
# for ch in phone:
#     output += digit_mapping.get(ch , "!") + " "
# print(output)

# function tutorial
# def greet_user():
#     print("Hi there")
#     print("Welcome on board")


# print("Start")
# greet_user()
# print("Finish")

# parameters tutorial
# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome on board")


# print("Start")
# greet_user("Senator", "smith")
# greet_user("Tolashe", "smith")
# print("Finish")

# keywords arguments
# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome on board")


# print("Start")
# greet_user(last_name="smith", first_name="john")
# print("Finish")

# return statement
# def square(number):
#     return number * number


# print(square(3))

# exeptions
# try:
#     age = int(input("age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print("Age can not be 0.")
# except ValueError:
#     print("Invalid value")

# comments
# 

# classes
# class Point:
#     def move(self):
#         print(move)
    
#     def draw(self):
#         print(draw)

# Point1 = Point()
# Point1.x = 10
# Point1.y = 20
# print(point1.x)

# constructors
