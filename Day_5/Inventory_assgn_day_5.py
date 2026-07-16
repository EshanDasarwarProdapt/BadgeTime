
# inv = []

# cat = 3
# prod = 4

# for i in range(cat):
#     cat = input(f"Enter name of category {i+1}: ")

#     prod = []
#     for j in range(prod):
#         product = input(f"Enter product {j+1} name: ")
#         qty = int(input(f"Enter quantity of {product}: "))

#         prod.append([product, qty])
    
#     inv.append([cat, prod])


# #to print the inventory

# for i in range(cat):
#     print(inv[i][0])

#     for j in range(prod):
#         print(inv[i][1][j][0], inv[i][1][j][1])



products = ["laptop", "mouse", "keyboard"]
print("Current products:", products)
x = input("Enter an urgent product name: ")
products.append(x)
print(products)
new_prod = input("Enter a new product name: ")
products.append(new_prod)
a = input("Enter a product name to remove: ")
products.remove(a)
print(products)

b = input("Enter a prod to be shipped: ")
print(f"{b} has been shipped.")
products.remove(b)
print(products)

c = input("Enter a product name to check quantity: ")
if c in products:
    print(f"Quantity of {c}: {products.count(c)}")
else:
    print(f"{c} is not in the inventory.")

products.sort()
print("Sorted products:", products)

products.reverse()
print("Reversed products:", products)

l = products.copy()
print("Copied products:", l)

l.clear()
print("Cleared copied products:", l)