# **Basic Functions**
# abc():Return the absolute value of a number.
print("~~~abc()~~~")
print(abs(-5))  # output: 5
print(abs(3.56))  # output 3.56
print()

# len():Returns the length (number of items) of an object (string, list, tuple, etc.)
print("~~~len()~~~")
nums = [11, 23.1, -4, -5]
print(len(nums))  # output: 4

my_string = "Hello world"
print(len(my_string))  # output: 11
print()

# max():Returns the largest item in an iterable or the largest of two or more arguments.
print("~~max()~~~")
numbers = [1, 4, 7, 3, 9, 2]
print(max(numbers))  # output: 9

print(max(10, 34, 20))  # output: 34
print()


# min():Returns the smallest item in an iterable or the smallest of two or more arguments.
print("~~~min()~~~")
numbers = [1, 4, 7, 3, 9, 2]
print(min(numbers))  # output: 1

print(min(10, 34, 20))  # output: 10
print()


# print():Displays output to the console.
print("~~~print()~~~")
print("Hello, world!")  # output: Hello, world!

x = 10
print("The value of x is:", x)  # output: The value of x is: 10
print()


# range(): Generates a sequence of numbers.
print("~~~range()~~~")
print("range():")
for i in range(5):  # generates numbers from 0 to 4
    print(i)  # output: 0 1 2 3 4
print()
for i in range(2, 10, 2):  # generates numbers from 2 to 9, stepping by 2
    print(i)  # output: 2 4 6 8
print()


# round(): Rounds a number to a specified number of decimal places.
print("~~~round()~~~")
print(round(3.14159, 2))  # output: 3.14

print(round(4.6))  # output: 5
print()


# sum(): Returns the sum of all items in an iterable.
print("~~~sum()~~~")
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # output: 15
print()


# type(): Returns the type of an object.
print("~~~type()~~~")
x = 10
print(type(x))  # Output: <class 'int'>

y = "Hello"
print(type(y))  # Output: <class 'str'>
print()


# **Type Conversion Functions**
# int(): Converts a value to an integer.
print("~~~int()~~~")
print(int("123"))  # Output: 123
print(int(3.14))  # Output: 3
print()


# float(): Converts a value to a floating-point number.
print("~~~float()~~~")
print(float("3.14"))  # Output: 3.14
print(float(5))  # Output: 5.0
print()


# str(): Converts a value to a string.
print("~~~str()~~~")
x = 10
print(str(x))  # Output: "10"
print()


# bool(): Converts a value to a boolean (True or False).
print("~~~bool()~~~")
print(bool(0))    # Output: False
print(bool(1))    # Output: True
print(bool(""))   # Output: False
print(bool("text"))  # Output: True
print()


# **Working with Iterables**
# enumerate(): Returns an enumerate object, which yields pairs of index and value when iterated.
print("~~~enumerate()~~~")
my_list = ["apple", "banana", "cherry"]
for index, value in enumerate(my_list):
    print(index, value)
# Output:
# 0 apple
# 1 banana
# 2 cherry
print()


# filter(): Filters items from an iterable based on a function.
print("~~~filter~~~")
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
print()


# map(): Applies a function to each item in an iterable.
print("~~~map()~~~")
numbers = [1, 2, 3]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9]
print()


# zip(): Aggregates elements from multiple iterables.
print("~~~zip()~~~")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
for name, age in zip(names, ages):
    print(name, age)
# Output:
# Alice 25
# Bob 30
# Charlie 28
print()


# **Other Important Functions**
# input(): Reads a line from input, converts it to a string, and returns it.
print("~~~input()~~~")
name = input("Enter your name: ")
print("Hello,", name)
print()


# open(): Opens a file.
print("~~~open()~~~")
with open("Upd_data_corr.csv", "r") as file:
    contents = file.read()
    print(contents)
print()



