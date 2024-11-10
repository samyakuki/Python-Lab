products = [('Laptop', 1000), ('Phone', 500), ('Tablet', 300)]
sorted_products = sorted(products, key=lambda x: x[1], reverse=True)
print(sorted_products)