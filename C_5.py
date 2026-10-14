# Function to convert Star (Wye) resistor values to Delta values
def star_to_delta(x, y, z):
    num = (x * y) + (y * z) + (z * x)
    d1 = num / z
    d2 = num / x
    d3 = num / y
    return (round(d1, 2), round(d2, 2), round(d3, 2))

# Test the function with sample values and display the result
ans = star_to_delta(10, 20, 30)
print("star_to_delta(10, 20, 30) ->", ans)
