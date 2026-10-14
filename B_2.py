# Get the total count of resistors from the user
count = int(input("How many resistors? "))

if count <= 0:
    print("The number of resistors must be greater than zero.")
else:
    total = 0.0
    val = 0.0
    
    # Loop through each resistor to get its value and add it to the total
    for i in range(1, count + 1):
        val = float(input(f"R{i}: "))
        total = total + val
        
    # Display the calculated total resistance
    print("Total resistance:", total, "ohms")
