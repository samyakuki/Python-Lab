documents = [
    {"apple", "banana", "cherry"},
    {"banana", "cherry", "date"},
    {"apple", "raisen", "almond"},
]
a=set()
for i in documents:
    a^=i
print(a)