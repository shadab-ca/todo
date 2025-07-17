def sum(a,b): 
    s = a + b
    return s
    
def sub(a,b):
    s = a-b
    return s
    
def mult(a,b):
    m = a*b
    return m

def div(a,b):
    d = a/b
    return d


def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd") 

def factorial(a):
    factorial = 1
    if  a < 0:
        print("sorry")
    elif a == 0:
        print("factorial")
    else:  
        for i in range(1,a + 1):
            factorial = factorial*i
        print("factorial",factorial)

def prime(num)
     naved = False
    if num == 0 or num == 1:
       print(num,"is not prime num")
    elif: num > 1:
      
      for i in range(2,num)
            
oper = int(input("opertion:"))
num1 = int(input("enter the num1:"))
num2 = int(input("ente the num2:"))
value = 0
if oper == 1:
    value =  sum(num1, num2)
elif oper == 2:
    value = sub(num1,num2)

elif oper == 3: 
    value = mult(num1,num2)

elif oper == 4:
    value = div(num1,num2)

elif oper == 5:
    value = factorial(num1)
    
elif oper == 6:
    check_even_odd(num1)
    check_even_odd(num2)    

elif oper = 7:
   value = prime  
    
print("value=",value)
    

 