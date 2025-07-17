a = int(input("enter thr num:"))
b = int(input("enter thr num:"))
def sum(a, b):
    s = a + b
    print("s =", s)
    return s
x = a
y = b
value = sum(y, x)
print("value =", value)

if value % 2 == 0:
    print("Even")
else:
   print("Odd")