import decimal

print(0.2 + 0.1 == 0.3)  # It is False

a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
c = decimal.Decimal('0.1') + decimal.Decimal('0.2')

print(a + b == c)
