# Function to convert a decimal number to its binary string representation
def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    b_str = ""
    while n > 0:
        rem = n % 2
        b_str = str(rem) + b_str  
        n = n // 2
        
    return b_str

# Test the conversion function with sample values
print("decimal_to_binary(10) ->", decimal_to_binary(10))
print("decimal_to_binary(25) ->", decimal_to_binary(25))
