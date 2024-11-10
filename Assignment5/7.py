def find_common_products(inventory1, inventory2):
    set1 = set(inventory1)
    set2 = set(inventory2)
    common_products = set1.intersection(set2)
    
    return common_products

warehouse1 = ["product1", "product2", "product3", "product4"]
warehouse2 = ["product3", "product4", "product5", "product6"]

common_products = find_common_products(warehouse1, warehouse2)
print("Common products:", common_products)
