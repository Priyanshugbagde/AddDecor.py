# To create a decorator in python

# Original simple function that adds two numbers
def addition1(n1, n2):
    print(n1)
    print(n2)
    print(n1 + n2)
    return n1 + n2

# Decorator to decorate and extend the original function
def decorate_output(func):
    # Inner function that wraps the original logic
    def wrapper(n1, n2, n3):
        # Decorative pattern before the addition result
        print(" * " * 30)
        print(" * " * 20)
        print(" * " * 10)
        print(" * " * 5)

        print("The first number is  : ", n1)
        print("The second number is : ", n2)
        print("The third number is  : ", n3)

        # Calling original 2-argument function, then adding the 3rd
        r = func(n1, n2) + n3
        print("The addition of the three numbers is:")
        print(r)

        # Decorative pattern after the result
        print(" * " * 30)
        print(" * " * 20)
        print(" * " * 10)
        print(" * " * 5)

        return r

    return wrapper  # Return the inner function

# Function call: normal, undecorated version
addition1(10, 20)

# Create a new decorated version of the original function
addDecor = decorate_output(addition1)

# Call the decorated version with 3 numbers
addDecor(10, 20, 30)

# ------------------------------
# Alternate way using decorator syntax (@...) directly above the function:
# Uncomment the lines below if you want to decorate it directly (but then it must accept 3 inputs)
#
# @decorate_output
# def addition1(n1, n2):
#     print(n1)
#     print(n2)
#     print(n1 + n2)
#     return n1 + n2

# addition1(10, 20, 30)
# ------------------------------
