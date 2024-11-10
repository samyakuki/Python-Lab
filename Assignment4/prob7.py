from operator import itemgetter

data = []
while True:
    entry = input("Enter name, age, height  or type 'done' to finish: ")
    if entry.lower() == 'done':
        break
    data.append(tuple(entry.split(",")))

data.sort(key=itemgetter(0, 1, 2))

print(data)
