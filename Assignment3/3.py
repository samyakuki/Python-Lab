num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
x, y = num1, num2
while y != 0:
    x, y = y, x % y
gcd = x
lcm = (num1 * num2) // gcd
print(f"The GCD of {num1} and {num2} is: {gcd}")
print(f"The LCM of {num1} and {num2} is: {lcm}")