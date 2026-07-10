# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

# A = Node(1)
# B = Node(2)
# A.next = B

# head = A

# cur = head

# while cur:
#     print(cur.val)
#     cur = cur.next

# print(eval("10+5"))

# a = 5
# b = 5
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# exp = input()
# res = eval(exp)
# print(res)


#Bitwise operators
# a = 10
# b = 6

# print(a & b)  # Bitwise AND
# print(a | b)  # Bitwise OR
# print(a ^ b)  # Bitwise XOR
# print(~a)     # Bitwise NOT
# print(a<<2)  # Left Shift
# print(a>>2)  # Right Shift

#Membership operator
# language = "python"
# print("y" in language)  # True
# print("z" in language)  # False


# bal = 100000
# amt = int(input("Enter the amount to withdraw( in multiples of 100 ): "))

# if amt < bal and amt % 100 ==0:
#     bal -= amt
#     print("Transaction successful. Remaining balance:", bal)
# else:
#     print("Transaction failed. Please check the amount and try again.")


# marks = int(input("Enter your marks: "))

# if marks >= 40:
#     print("You have passed the exam.")
# else:
#     print("You have failed the exam.")



# username = "admin"
# password = "password"

# input_username = input("Enter username: ")
# input_password = input("Enter password: ")

# count = 1

# while count<=3:
#     if input_username == username and input_password == password:
#         print("Login successful!")
#         break
#     else:
#         print("Invalid username or password. Please try again.")
#         count += 1
#         if count <= 3:
#             input_username = input("Enter username: ")
#             input_password = input("Enter password: ")




# l1 = ["m", "na", "i", "ke"]
# l2 = ["y", "me", "s", "lly"]
# l3 = [i+j for i, j in zip(l1,l2)]
# print(l3)


# l1 = ["mike", "" , "hello"]

# r = list(filter(None, l1)  )

# print(r)




# stores = 3
# days = 7

# for i in range(stores):
#     total = 0
#     for j in range(days):
#         s = int(input(f"Enter sales for store {i+1} on day {j+1}: "))
#         total += s
#     print(f"Total sales for store {i+1}: {total}")

# l1 = []
# l2 = []
# l3 = []

# a = int(input())
# if a == 1:
#     for i in range(1,8):
#         l1.append(i)
# elif a == 2:
#     for i in range(1,8):
#         l2.append(i)
# elif a == 3:
#     for i in range(1,8):
#         l3.append(i)
# print(sum(l1))
# print(sum(l2))
# print(sum(l3))





# cat = 3
# prod = 4

# inventory = []

# for i in range(cat):
#     category = input(f"Enter name of category {i+1}: ")

#     products = []

#     for j in range(prod):
#         product = input(f"Enter product {j+1} name: ")
#         qty = int(input(f"Enter quantity of {product}: "))

#         products.append([product, qty])

#     inventory.append([category, products])

# print("--- Inventory ---")

# for i in range(cat):
#     print(f"Category: {inventory[i][0]}")

#     for j in range(prod):
#         print(
#             f"Product: {inventory[i][1][j][0]}, "
#             f"Quantity: {inventory[i][1][j][1]}"
#         )

# print(inventory)



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