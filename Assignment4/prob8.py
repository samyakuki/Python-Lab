import math

post = [0, 0]

steps = input("Enter steps: ").split(" ")

for i in range(0, len(steps), 2):
    direction = steps[i]
    step = int(steps[i + 1])
    
    if direction == "UP":
        post[0] += step
    elif direction == "DOWN":
        post[0] -= step
    elif direction == "LEFT":
        post[1] -= step
    elif direction == "RIGHT":
        post[1] += step

distance = math.sqrt(post[0]**2 + post[1]**2)
print(round(distance))
