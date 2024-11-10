n = int(input("Enter a number "))

def fibonacci(a, b, n):
    u = ()
    w = []
    x = {}
    seq = []
    for i in range(n):
        seq.append(a)
        a, b = b, b + a
    print(seq)
    print("Number of local variables inside fibonacci:", len(locals())) 

fibonacci(0, 1, n)
