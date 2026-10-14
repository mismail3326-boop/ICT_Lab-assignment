def parallel_resistance(items):
    total = 0
    for x in items:
        total += 1 / x
    return 1 / total

lst = []
print("Enter resistor values one by one. Enter 0 when finished.")
while True:
    try:
        n = float(input("Enter resistor value (ohms): "))
        if n == 0:
            break
        lst.append(n)
    except ValueError:
        print("Please enter a valid value.")

# Call the function and show the result
ans = parallel_resistance(lst)
print(f"parallel resistance({lst}):{ans}")
