def bank(n):
    balance = n  # Use a local variable to track balance

    def depo(x):
        nonlocal balance
        balance += x
        return f"depo {x} , bal {balance}"

    def withdraw(x):
        nonlocal balance
        if balance >= x:
            balance -= x
            return f"withdraw {x} , bal {balance}"
        else:
            return "insuff"

    return lambda : None,depo,withdraw

# Usage
a = bank(100)
_,depo,withdraw=a;
 
print(depo(60))