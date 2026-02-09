def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

def factorial(a):
    if a < 0:
        return "sorry"
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    return fact

def prime(num):
    if num == 0 or num == 1:
        print(num, "is not a prime number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                return
        print(num, "is a prime number")


oper = int(input("operation: "))
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

value = None

if oper == 1:
    value = add(num1, num2)
elif oper == 2:
    value = sub(num1, num2)
elif oper == 3:
    value = mult(num1, num2)
elif oper == 4:
    value = div(num1, num2)
elif oper == 5:
    value = factorial(num1)
elif oper == 6:
    check_even_odd(num1)
    check_even_odd(num2)
elif oper == 7:
    prime(num1)

if value is not None:
    print("value =", value)


 
