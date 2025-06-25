````
# Decorators in Python: Adding Functionality with Style

## Description

This Python program demonstrates how to use **decorators** to add extra functionality to an existing function, without modifying its original code. The program includes:

- A basic function `addition1()` that adds two numbers.
- A decorator `decorate_output()` that:
  - Adds a center-reducing decorative pattern before and after execution.
  - Prints inputs clearly.
  - Adds a third number to the sum using the decorated version.

Both manual and `@decorator` usage styles are shown (the `@` part is commented for flexibility).

---

## Code Overview

### Original Function
```python
def addition1(n1, n2):
    print(n1)
    print(n2)
    print(n1 + n2)
    return n1 + n2
````

### Decorator

```python
def decorate_output(func):
    def wrapper(n1, n2, n3):
        print(" * " * 30)
        print(" * " * 20)
        print(" * " * 10)
        print(" * " * 5)

        print("The first number is  : ", n1)
        print("The second number is : ", n2)
        print("The third number is  : ", n3)

        r = func(n1, n2) + n3
        print("The addition of the three numbers is:")
        print(r)

        print(" * " * 30)
        print(" * " * 20)
        print(" * " * 10)
        print(" * " * 5)

        return r
    return wrapper
```

### Applying the Decorator

```python
addDecor = decorate_output(addition1)
addDecor(10, 20, 30)
```

### Optional `@` Syntax

```python
# @decorate_output
# def addition1(n1, n2):
#     ...
# addition1(10, 20, 30)
```

---

## Output

```
10
20
30
 *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  *  * 
 *  *  *  *  * 
The first number is  :  10
The second number is :  20
The third number is  :  30
10
20
30
The addition of the three numbers is:
60
 *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  *  *  * 
 *  *  *  *  * 
```

---

## Notes

* The original function remains unchanged and reusable.
* The decorator adds formatting, messaging, and logic enhancements.
* Ideal for wrapping logging, validation, or formatting around functions without editing them.

```
```
