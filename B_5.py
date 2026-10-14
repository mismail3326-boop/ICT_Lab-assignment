# Initialize counters
n1 = 0
n5 = 0
bad = 0

while True:
    x = float(input("Enter resistance (0 to stop): "))
    
    # Exit loop on zero and increment counters based on range
    if x == 0:
        break
        
    if 99.0 <= x <= 101.0:
        n1 += 1
    elif 95.0 <= x <= 105.0:
        n5 += 1
    else:
        bad += 1

# Print the final counts
print("1% tolerance:", n1)
print("5% tolerance:", n5)
print("Reject:", bad)
