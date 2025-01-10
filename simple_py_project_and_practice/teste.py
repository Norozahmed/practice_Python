# # # # # # # # x = int(input())
# # # # # # # # y = int(input())
# # # # # # # #
# # # # # # # # x = x // y
# # # # # # # # y = y // x
# # # # # # # #
# # # # # # # # print(y)
# # # # # # # #
# # # # # # #
# # # # # # # x = int(input())
# # # # # # # y = int(input())
# # # # # # #
# # # # # # # x = x / y
# # # # # # # y = y / x
# # # # # # #
# # # # # # # print(y)
# # # # # # #
# # # # # #
# # # # # # x = int(input())
# # # # # # y = int(input())
# # # # # #
# # # # # # x = x % y
# # # # # # x = x % y
# # # # # # y = y % x
# # # # # #
# # # # # # print(y)
# # # # #
# # # # #
# # # # # x = input()
# # # # # y = int(input())
# # # # #
# # # # # print(x * y)
# # # #
# # # # z = y = x = 1
# # # # print(x, y, z, sep='*')
# # # #
# # #
# # # y = 2 + 3 * 5.
# # # print(y)
# # #
# #
# # x = 1 / 2 + 3 // 3 + 4 ** 2
# # print(x)
# #
#
#
# x = int(input())
# y = int(input())
#
# print(x + y)
import random

# black_sheep = 4
# white_sheep = 2
# print(black_sheep == 2 * white_sheep)

# number_of_lions = 5
# number_of_lionesses = 4
# answer = number_of_lions >= number_of_lionesses
# print(answer)

# n = int(input())
# print(n >= 100)

# weather = input("How's the weather? ")
#
# if weather == "good":
#     print("Let's go for a Walk!")
# print("have a lunch!")

# sheep_counter = 150  # Assign a value to sheep_counter

# if sheep_counter >= 120:
#     print("Making a bed...")  # Replace with your actual functions
#     print("Taking a shower...")
#     print("Sleeping and dreaming...")
#     print("Feeding the sheepdogs...")
# else:
#     print("Feeding the sheepdogs...") # If less than 120


# condition = int(input("Enter a number: "))
#
# if condition:
#     print("Condition is True.")
# else:
#     print("Condition is False!")

# print("Note: 1 = Yes and 0 = No")
# the_weather_is_good = int(input("Is whether good? "))
# nice_restaurant_is_found = None
# tickets_are_available = None
#
# if the_weather_is_good:
#     nice_restaurant_is_found = int(input("Is there a nice restaurant? "))
#     if nice_restaurant_is_found:
#         print("have lunch")
#     else:
#         print("eat sandwich")
# else:
#     tickets_are_available = int(input("Are tickets available? "))
#     if tickets_are_available:
#         print("go to the theater!")
#     else:
#         print("go for shopping")

# print("Note: 1 = Yes and 0 = No")
# the_weather_is_good = int(input("Is whether good? "))
# tickets_are_available = int(input("are tickets available? "))
# table_is_available = int(input("is there any table available? "))
#
# if the_weather_is_good:
#     print("go for a walk")
# elif tickets_are_available:
#     print("go to the theater")
# elif table_is_available:
#     print("go for lunch")
# else:
#     print("play chess at home")


# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2: larger_number = number1
# else: larger_number = number2
#
# # Print the result
# print("The larger number is:", larger_number)


# Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# # We temporarily assume that the first number
# # is the largest one.
# # We will verify this soon.
# largest_number = number1
#
# # We check if the second number is larger than the current largest_number
# # and update the largest_number if needed.
# if number2 > largest_number:
#     largest_number = number2
#
# # We check if the third number is larger than the current largest_number
# # and update the largest_number if needed.
# if number3 > largest_number:
#     largest_number = number3
#
# # Print the result
# print("The largest number is:", largest_number)

# largest_number = -999999999
# number = int(input())
# if number == -1:
#     print(largest_number)
#     exit()
# if number > largest_number:
#     largest_number = number
# # Go to line 02


# plant = input("Write here: ")
#
# if plant != "Spathiphyllum":
#     print(f"Spathiphyllum not {plant}")
#
# elif plant == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best ever!")
#
# elif plant.lower():
#     print("No, i want a big Spathiphyllum!")

# name = input("Enter flower name: ")
#
# if name == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif name == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not", name + "!")


# largest_number = -99999999
#
# number = int(input("enter a number or type -1 to stop: "))
#
# while number != -1:
#     if number > largest_number:
#         largest_number = number
#
#     number = int(input("Enter a number or type -1 to stop: "))
#
# print("The largest number is", largest_number)


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.


# odd_numbers = 0
# even_numbers = 0
#
# # Read the first number.
# number = int(input("Enter a number or type 0 to stop: "))
#
# # 0 terminates execution.
# while number != 0:
#     # Check if the number is odd.
#     if number % 2 == 1:
#         # Increase the odd_numbers counter.
#         odd_numbers += 1
#     else:
#         # Increase the even_numbers counter.
#         even_numbers += 1
#     # Read the next number.
#     number = int(input("Enter a number or type 0 to stop: "))
#
# # Print results.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)


# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

# counter = 5
# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

# import random
# secret_number = random.randint(1, 100)
#
#
# while True:
#     guess_number = int(input("Enter you number: "))
#     if guess_number != secret_number:
#         print("Ha ha! You're stuck in my loop!")
#         if guess_number > guess_number:
#             print("your number is greater")
#         else:
#             print("Your number is less")
#     else:
#         print(secret_number)
#         print("Well done, mugle! You are free now.")
#         break


# secret_number = 777  # The magician's secret number
#
# print(
#     """
# +================================+
# | Welcome to the number guessing game! |
# +================================+
# """
# )
#
# while True:
#     try:
#         guess = int(input("Enter an integer number: "))
#     except ValueError:
#         print("Invalid input. Please enter an integer.")
#         continue  # Go back to the beginning of the loop
#
#     if guess != secret_number:
#         print("Ha ha! You're stuck in my loop!")
#     else:
#         print(secret_number)
#         print("Well done, muggle! You are free now.")
#         break  # Exit the loop


# i = 0
# while i < 10:
#     i += 1
#     print(i, end=",")

# for i in range(100):
#     # do_something()
#     print(i)


# for i in range(2, 1):
#     print("The value of i is currently", i)

# largest_number = -99999999
# counter = 0
#
# while True:
#     number = int(input("Enter a number or type -1 to end the program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number
#
# if counter != 0:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")


# largest_number = -99999999
# counter = 0
#
# number = int(input("Enter a number or type -1 to end program: "))
#
# while number != -1:
#     if number == -1:
#         continue
#     counter += 1
#
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end the program: "))
#
# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

#
# while True:
#     word = input("Enter a word: ")
#     if word == "chupacabra":
#         print("You've successfully left the loop.")
#         break  # Exit the loop
    # No output for other words


blocks = int(input("Enter the number of blocks: "))
height = 0
blocks_needed = 1

#
while blocks >= blocks_needed:
    height += 1
    blocks -= blocks_needed
    blocks_needed += 1
#

print("The height of the pyramid:", height)




