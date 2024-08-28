s = input("Enter a sentence: ")
words = s.split(" ")
print("The sentence has " + str(len(words)) + " words")
digits = 0
lower_case = 0
upper_case = 0
for i in words:
    for j in i:
        if j.isupper():
                upper_case += 1
        if j.islower():
            lower_case += 1
        if j.isnumeric():
            digits += 1
print("This sentence has " + str(digits) + " digits")
print(str(upper_case) + " upper case letters")
print(str(lower_case) + " lower case letters")


