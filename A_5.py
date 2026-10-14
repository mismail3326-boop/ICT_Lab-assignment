# Get three resistor values from the user
a = float(input("Enter first resistor value: "))
b = float(input("Enter second resistor value: "))
c = float(input("Enter third resistor value: "))

# Code for finding the largest
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Code for finding the smallest
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Printing results
print("Smallest resistor:", smallest)
print("Largest resistor:", largest)
