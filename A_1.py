# Ask user for value for V AND R
v = float(input("Enter voltage:"))
r = float(input("Enter resistance:"))

if r<0:
    print('invalid')
else:
    i = v / r #current formula
    print("current:", i)
    
    if i > 2:
       print("Fuse will blow")
    else:
       print("Circuit is safe")
