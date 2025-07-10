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
    
print("value=",value)
    

 