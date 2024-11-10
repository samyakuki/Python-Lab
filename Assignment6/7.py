n=int(input("Enter a number "))
def fibonacci(a,b,n):
    seq=[]
    for i in range(n):
        seq.append(a)
        a,b=b,b+a
    print(seq)

fibonacci(0,1,n)