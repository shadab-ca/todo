a = float(input("enter thr num:"))
b = float(input("enter thr num:"))
def div(a,b):
    d = a/b
    print("d=",d)
    return d
  
x = a
y = b
value = div(a,b)
print("value=",value)
if value % 2 == 0:
      print("even")
else:
    print("odd")
  