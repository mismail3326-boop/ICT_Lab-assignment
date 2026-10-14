# ask user for current value
current = float(input("Enter current value: "))

#if current is negative or positive and decide its direction
if current > 0:
    print("Current flows from A to B")
elif current < 0:
    print("Current flows from B to A")
else:
    print("No current flows")
