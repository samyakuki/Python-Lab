def mul2(x):
    return x*2
def add3(x):
    return x+3

def pipe(fun1,fun2,x):
    mul=fun1(x)
    result=fun2(mul)
    return result

a=pipe(mul2,add3,5)
print(a)