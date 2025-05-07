# to find the GCD of 2 numbers.
a = 10
b = 26

while b != 0:
    temp = b
    b = a % b
    a = temp

print(a, "is the GCD")
