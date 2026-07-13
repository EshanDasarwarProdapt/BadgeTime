# def square(num):
#     return num ** 2

# print(square(5)) 

# def is_palindrome(string):
#     string = string.lower().replace(" ", "")
#     return string == string[::-1]

# word = input("Enter a word to check if it's a palindrome: ")
# if is_palindrome(word): 
#     print(f"{word} is a palindrome.")
# else:
#     print(f"{word} is not a palindrome.")



# add = lambda a,b : a + b
# sub = lambda a,b : a - b

# print("Addition of 5 and 3:", add(5,3))
# print("Subtraction of 5 and 3:", sub(5,3))

find_largest_word = lambda text: max(text.split(), key=len)
# text = input("Enter a sentence: ")
# largest_word = find_largest_word(text)
# print(f"The longest word in the sentence is: {largest_word}")



import time

text  = input("Enter a sentence: ")
start_time = time.perf_counter()
largest_word = find_largest_word(text)


end_time = time.perf_counter()
print(f"Largest word: {largest_word}")
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.6f} seconds")


