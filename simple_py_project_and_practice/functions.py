
# Scopes in Python

# The scope of a name (e.g., a variable name) is the part of a code where the name is properly recognizable.
# For example, the scope of a function's parameter is the function itself. The parameter is inaccessible outside the function.
#
# def scope_test():
#     x = 123
#
#
# scope_test()
# print(x)        #will cause an NameError: name 'x' is not defined


# var = 10


# def my_function():
#     print("Do I know that variable?", var)
#
#
# var = 1
# my_function()
# print(var)


# def my_function():
#     var = 2
#     print("Do I know that variable", var)
#
#
# var = 1
# my_function()     # output: Do i know that variable 2
# print(var)  # output: 1

# the 'var' variable created inside the function is not the same as when defined outside it ‒ it seems that there two different variables of the same name;
# moreover, the function's variable shadows the variable coming from the outside world.


# def my_function():
#     var = 2
#     # print("Do I know that variable", var)
#     print(f"{var} + {var2} = {var + var2}")

# var2 = 5
# var = 1
# my_function()     # output: Do i know that variable 2
# print(var)


# Functions and scopes: the global scope


# def my_function():
#     global var
#     var = 2
#     print("THe value of var is", var) 

# ~~~~~~~~~~

# var = 3
# my_function()
# print(var)

# def func(n):
#     print("I got", n)
#     n += 1
#     print("I have", n)

# var = 1
# func(var)
# print(var)

# ~~~~~~~~~~

# def my_func(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)

# my_list_2 = [2, 3]
# my_func(my_list_2)
# print("Print #5:", my_list_2)

'''
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]   # pay attention to this line
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2) '''

# ~~~~~~~~~~

# var = 2

# def mult_by_var(x):
#     return x * var

# print(mult_by_var(7))

# # or

# def mult(x):
#     var = 2
#     return x * var

# print(mult(7))


# def mult(x):
#     var = 2
#     return x * var

# var = 3
# print(mult(7))  # output: 14
# print(7 * var)  # output: 21


# ~~~~~~~~~~

# def adding(x):
#     var = 7
#     return x + var

# print(adding(4)) # output: 11
# print(var) # NameError

# OR use gloabl keyword followed by variable name to make the variable's scope global, e.g.:

# var = 2
# print(var) # output: 2

# def return_var():
#     global var
#     var = 5
#     return var

# print(return_var()) # output: 5
# print(var) # output: 5

# ~~~~~~~~~~

# name = input("What is your name? ")

# def ask(name):
#     age = input(f"Hey, {name} how old are? ")
#     return f"{name} is {age} years old"
# print(ask(name))
# # print(f"Thank you {name} for your response")

# # my_name = {name}
# ask = input(f"{name} Do you have any questions?")

# if ask == "yes":
#     topic = input("What is your question?")
#     print(f"You're asking about {topic}. That's a broad topic, is there anything specific you'd like to focus on?")    

# elif ask == "no":
#     print(f"Thank you for your time {name}")
# else:
#     print("I am sorry, I did not understand your response")

# ~~~~~~~~~~

# Sample function: Evaluate the BMI

# def bmi(weight, height):
#     return weight / height ** 2

# w = float(input("Enter your weight in kg: "))
# h = float(input("Enter your height in meters: "))
# print(bmi(w, h)) 


# Evaluating BMI and converting imperial units to metric units

# def bmi(weight, height):
#     if height < 1.0 or height > 2.5 or \
#         weight < 20 or weight > 200:
#         return None
    
#     return weight / height ** 2

# print(bmi(352, 1.5)) # output: None


# number = [1, 2, 5]
# for num in number:
#     if num == 5:
#         print("5 found!")
#         break
# else:
#     print("5 not found!") 



# Calculate weight in kg from lb
# def lb_to_kg(lb):
#     return lb * 0.45359237 # 1 lb is equal to 0.45359237 kg

# weight = float(input("Enter your weight in lb: "))
# print(lb_to_kg(weight))



# now let's try it for feet and inches : 1ft = 0.3048m and 1 inch = 0.0254m

# def ft_and_inch_to_m(ft, inch):
#     return ft * 0.3048 + inch * 0.0254

# ft = int(input("Enter the feet: "))
# inch = int(input("Enter the inches: "))
# print(ft_and_inch_to_m(ft, inch))


# def ft_to_m(ft):
#     return ft * 0.3048

# ft = int(input("Enter the feet: "))
# print(ft_to_m(ft))


# def inch_to_m(inch):
#     return inch * 0.0254

# inch = float(input("Enter the inches: "))
# print(inch_to_m(inch))




# now let's try the BMI of a person by calculating height and weight

# def fit_and_inch_to_m(ft, inch=0):
#     return ft * 0.3048 + inch * 0.0254

# def lb_to_kg(lb):
#     return lb * 0.45359237

# def bmi(weight, height):
#     if height < 1.0 or height > 2.5 or \
#         weight < 20 or weight > 200:
#         return None
    
#     return weight / height ** 2

# lb = float(input("Enter your weight in lb: "))  
# ft = float(input("Enter the feet: "))
# inch = float(input("Enter the inches: "))

# print(bmi(weight = lb_to_kg(lb), height = fit_and_inch_to_m(ft, inch))) # output: 55.0

# ~~~~~~~~~~

# def is_a_trangle(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True

# print(is_a_trangle(1, 1, 1)) # output: True
# print(is_a_trangle(1, 1, 2)) # output: False

# more compact version of the above code
# def is_a_trangle(a, b, c):
#     if a + b <= c or b + c <= a or c + a <= b:
#         return False
#     return True

# print(is_a_trangle(1, 1, 1)) # output: True
# print(is_a_trangle(1, 1, 2)) # output: False

# # compact it even more
# def is_a_trangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b

# print(is_a_trangle(1, 1, 1)) # output: True
# print(is_a_trangle(1, 1, 2)) # output: False


# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b

# a = float(input("Enter the first side of the triangle: "))
# b = float(input("Enter the second side of the triangle: "))
# c = float(input("Enter the third side of the triangle: "))
# if is_a_triangle(a, b, c):
#     print("Yes, it is a triangle.")
# else:
#     print('Not. it can\'t be a trangle')


# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b

# def is_a_right_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return False
#     if c > a and c > b:
#         return c ** 2 == a ** 2 + b ** 2
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2
#     return b ** 2 == a ** 2 + c ** 2

# print(is_a_right_triangle(5, 3, 4)) # output: True
# print(is_a_right_triangle(1, 3, 4)) # output: False


# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b

# def heron(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5

# def area_of_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return None
#     return heron(a, b, c)

# print(area_of_triangle(1., 1., 2. ** 0.5)) # output: 0.49999999999999983

# ~~~~~~~~~~

# Sample functions: Factorials

# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
    
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product

# for n in range(1, 6):
#     print(n, factorial_function(n))



# Fibonacci numbers
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
# 
# 
# for n in range(1, 10):  # testing
#     print(n, "->", fib(n))


# Resursion
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1

#     elam_1 = elam_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elam_1 + elam_2
#         elam_1, elam_2 = elam_2, the_sum
#     return fib(n - 1) + fib(n - 2)  
#     return the_sum

# for n in range(1, 10):
#     print(n, "->", fib(n))



# summary

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n -1)

# number = int(input("Enter a number: "))
# print(factorial(number) )


# def factorial(n):
#     return n * factorial(n -1)

# # number = int(input("Enter a number: "))
# print(factorial(4))


def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
    
number = int(input("Enter a number for recursion: "))
print(fun(number))
