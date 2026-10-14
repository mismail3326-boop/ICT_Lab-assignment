# List of voltage readings
data = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

# Initialize tracking variables
above_limit = 0
total = 0.0
total_count = 0
max_val = 0
min_val = 0

# Loop through each voltage value in the dataset
for val in data:
    total += val
    total_count += 1
    
    # Count values greater than 3.2 V
    if val > 3.2:
        above_limit += 1
        
    # Track the highest reading
    if val > max_val:
        max_val = val
        
    # Track the lowest reading
    if val < min_val:
        min_val = val

# Compute the average value
avg = total / total_count

# Display the final results
print(f"(a) Readings above 3.2 V: {above_limit}")
print(f"(b) Highest reading: {max_val} V")
print(f"(c) Lowest reading: {min_val} V")
print(f"(d) Average reading: {avg} V")
