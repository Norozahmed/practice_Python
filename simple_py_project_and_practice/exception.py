# try:
#     value = int(input("Enter a natural number: "))
#     print('The reciprocal of', value, 'is', 1/value)
# except ValueError:
#     print("Only integer Numbers Allowed!")  
# except ZeroDivisionError:
#     print('can\'t accept 0') 
# except:
#     print("Sorry, strange behaviour attracted") 


# l = ["harry","larry", "jerry","Carry"]
# print(len(l)) 

# try:
#     short_list = [1] 
#     one_value = short_list[0.5]
# except TypeError:
#     print("TypeError") 

# try:
      ## TypeError: Operations on incompatible types
#     num = int(input("Enter a number: "))
#     result = num + 'hello'
# except TypeError as e:
#     print(f"TypeError caught: {e}")

## NameError: Using an undefined variable
# try:
#     print(This_name_is_no_available)

# except NameError as e:
#     print(f"NameError_caught: {e}")


## IndexError: Accessing an invalid index in a sequence
# try:
#     my_list = [1, 2, 3]
#     ind = int(input("Enter Index Number: "))
#     print(my_list[ind])
# except IndexError as e:
#     print(f"IndexError_Caught: {e}")


## KeyError: Accessing a non-existent key in a dictionary
# try:   
#     my_dict = {"a": 1, "b": 2}
#     keey = input("Enter Key: ") 
#     print(my_dict[keey])
# except KeyError as e:
#     print(f"KeyError_Caught: {e}")


## ValueError: Invalid value for a specific operation
# try:
#     num = int("abc")
# except ValueError as e:
#     print(f"ValueError_Caught: {e}")


## ZeroDivisionError: Trying to open a non-existent file
# try:
#     num = int(input("Enter a number: ")) #if 0, will raise error
#     result = 10 / num
#     print(result)  
# except ZeroDivisionError as e:
#     print(f"ZeroDivisionError_Caught: {e}")


## FileNotFoundError: Trying to open a non-existant file
# try:
#     with open("nonexistent_file.txt", "r") as f:
#         content = f.read()
# except FileNotFoundError as e:
#     print(f"FileNotFoundError_Caught: {e}")


# try:
#         # 8. IOError (more general file error, can include PermissionError):
#         # Trying to write to a read-only file (example requires file setup)
#         # For simplicity, we'll simulate a permission error here.
#         raise PermissionError("Simulated permission denied")

# except IOError as e:  # Using IOError to catch various file-related errors
#         print(f"IOError caught: {e}")
# except PermissionError as e:
#         print(f"PermissionError caught: {e}")


# try:
#       #9. OverflowError: result of an arithmetic operation is too large to be expressed
#       import math
#       print(math.exp(1000))
# except OverflowError as e:
#       print(f"OverflowError caught: {e}")

# try:
#       #10. ImportError: module not found
#       import non_existent_module
# except ImportError as e:
#       print(f"ImportError caught: {e}")


# try:
#       #11. KeyboardInterrupt: User interrupt (Ctrl+C)
#       input("Press Enter to continue or Ctrl+C to interrupt: ")
# except KeyboardInterrupt:
#       print("KeyboardInterrupt caught. Program interrupted by user.") 

## AttributError: When User try to activate a method which doesn't exist in an item you're dealing with.
# try:
#     short_list = [1]
#     short_list.append(2)
#     short_list.nonexistent_method()
#     print(short_list)
# except AttributeError as e:
#     print(f"AttributError_Caught: {e}")   


# try:
#     # 13. SyntaxError: Invalid Python syntax (this is tricky to catch directly)
#     # The following would cause a SyntaxError during parsing, *before* runtime.
#     # To handle it, you'd need to use exec() or compile(), which is generally not recommended
#     # for handling user input due to security risks (code injection).
#     # Instead, I'll demonstrate a more practical scenario: syntax errors in eval()
#     code_string = "print(1 +" # Incomplete expression
#     eval(code_string)
#
# except SyntaxError as e:
#         print(f"SyntaxError_Caught (in eval()): {e}")

# try:
#     # A more practical example of handling potential errors from eval()
#     user_input = input("Enter a Python expression: ")
#     result = eval(user_input)
#     print(f"Result: {result}")
# except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e: # Catching multiple exceptions
#     print(f"Invalid expression: {e}")
# except Exception as e: # Catching any other exception
#     print(f"An unexpected error occurred: {e}")




# temperature = float(input('Enter current temperature:'))
# 
# if temperature > 0:
#     print("Above zero")
# elif temperature < 0:
#     print("Below zero")
# else:
#     print("Zero")


## eval() function
# x = 5
# result = eval("x + 3")  # Evaluates "5 + 3"
# print(result)  # Output: 8

# expression = "2 * (10 - 4)"
# result = eval(expression)
# print(result)  # Output: 12

# expression = "pow(2, 3)" #Using function
# result = eval(expression)
# print(result) #Output: 8

# expression = "[1,2,3,4]" #Creating list
# result = eval(expression)
# print(result) #Output: [1, 2, 3, 4]

# expression = "{'a':1, 'b':2}" #Creating dictionary
# result = eval(expression)
# print(result) #Output: {'a': 1, 'b': 2}

# a = eval(input("Enter first value: "))  
# b = eval(input("Enter second value: "))
# print(a + b)   

while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Wrong value or No division by zero rule broken.")
    except:
        print("Sorry, something went wrong...")


