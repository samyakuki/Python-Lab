class Seven:
    def __init__(self, n):
        self.n = n

    def generator(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

n = 50
div_seven =Seven(n)
for num in div_seven.generator():
    print(num)
