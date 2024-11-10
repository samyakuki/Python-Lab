def polynomial_creator(coefficients):
    def polynomial(x):
        result = 0
        n = len(coefficients) - 1
        for i, coeff in enumerate(coefficients):
            result += coeff * (x ** (n - i))
        return result
    return polynomial

poly = polynomial_creator([2, 3, 4])
result = poly(5)
print(result)
