def memorize_fact():
    cache={}
    def fact(n):
        if n in cache:
            return cache[n]
        if n==0 or n==1:
            return 1
        else:
            return n*fact(n-1)
    return fact

a=memorize_fact()
print(a(5))