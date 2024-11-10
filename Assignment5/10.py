s = {1, 2, 3}
power_set = [[]]

for elem in s:
    power_set += [subset + [elem] for subset in power_set]

power_set = [set(subset) for subset in power_set]
print(power_set)
