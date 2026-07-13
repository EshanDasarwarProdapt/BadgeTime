l = []

numbers = list(map(int, input("Enter the numbers separated by space: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

squared_even_numbers = list(map(lambda x: x ** 2, even_numbers))
print("Squared even numbers:", squared_even_numbers)