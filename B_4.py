voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
#iniatializing
max_len = 1
best_start = voltages[0]
best_end = voltages[0]
current_len = 1
current_start = voltages[0]
current_end = voltages[0]
#FOR loop and nested if
for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        if current_len == 1:
            current_start = voltages[i - 1]
        current_len += 1
        current_end = voltages[i]
    else:
        if current_len > max_len:
            max_len = current_len
            max_start = current_start
            max_end = current_end
        current_len = 1
        current_start = voltages[i]
        current_end = voltages[i]
if current_len > max_len:
    max_len = current_len
    best_start = current_start
    best_end = current_end

print(f"Longest continuous drop: {max_len} minutes")
print(f"Started at: {best_start} V")
print(f"Ended at: {best_end} V")
