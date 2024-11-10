def fun(x):
    global a
    a=5
    print(a)

def mod_fun(x):
    a=7
    print(a)

a=3
print(a)
fun(a)
mod_fun(a)