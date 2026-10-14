# Function to calculate unloaded and loaded voltage divider outputs
def load_divider(v, a, b, c):
    vu = v * (b / (a + b))
    eq = (b * c) / (b + c)
    vl = v * (eq / (a + eq))
    return (vu, vl)

# Test the function with sample values and print the result
ans = load_divider(12, 1000, 1000, 500)
print("loaded_divider(12, 1000, 1000, 500) ->", ans)
