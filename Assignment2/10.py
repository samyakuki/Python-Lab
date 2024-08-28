s = input("Enter a value:")
print("Palindrome" if s == s[::-1] else "Not Palindrome")

for i in set(s):
    print(str(i) + " appears " + str(s.count(i)) + " times ")