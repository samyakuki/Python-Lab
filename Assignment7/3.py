def fun(x):
    def mul(n):
        return x*n
    return mul

a=fun(4)
print(a(5))