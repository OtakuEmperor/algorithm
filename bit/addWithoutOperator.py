x = int(input("x: "))
y = int(input("Y: "))

while y != 0:
    carry = x & y
    x = x ^ y
    y = carry << 1

print(x)
