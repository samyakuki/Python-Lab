from functools import partial

two=partial(pow,exp=2)
print(two(5))