def is_divisble_5(n :str) -> int:
    return int(n, 2) % 5 == 0

nums = list(input(("Enter numbers:")).split(','))

output = ""
for i in nums:
    if is_divisble_5(i):
        output += i + ","
        
print(output[:-1])