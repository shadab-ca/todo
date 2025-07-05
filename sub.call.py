a = int(input("enter the num:"))
b = int(input("enter thr num:"))
def sub(a,b):
    s = a - b
    print("s=",s)
    return  s
    
x = a 
y = b
value = sub(a,b)
print("value=",value)

if value % 2 == 0:
   print("even")
else:
    print("odd")