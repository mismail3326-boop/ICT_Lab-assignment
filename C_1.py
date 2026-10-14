# Define functions for electrical calculations
def ohms_current(v, r):
    return v / r

def power_dissipated(i, r):
    return (i ** 2) * r

# Get user input values
v = float(input("input voltage:"))
r = float(input("input resistance:"))

# Compute current and power by calling the functions
curr = ohms_current(v, r)
pwr = power_dissipated(curr, r)
i = curr

# Display the final results
print(f"Current = {curr} A")
print(f"Power = {pwr} W")
