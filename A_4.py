
a = int(input("Enter bit A: "))
b = int(input("Enter bit B: "))

if a not in (0, 1) or b not in (0, 1):
    print("Bits should be 0 or 1")
else:
    andoutput = a and b
    oroutput = a or b
    if a != b:
        xoroutput=1
    else:
        xoroutput=0


# Print results
print("and:",andoutput)
print("or:",oroutput)
print("xor:",xoroutput)
