C, H = 50, 30
D = list(map(int, input("Enter D values:").split(',')))

Q = []

for i in D:
    value = int(((2 * C * i) // H) ** 0.5)
    Q.append(value)

print(Q)