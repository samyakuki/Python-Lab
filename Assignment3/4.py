import math
def ballscollide(ball1, ball2):
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance <= (r1 + r2)
ball1 = (1, 9, 1)
ball2 = (4, 5, 1)
print(ballscollide(ball1, ball2))