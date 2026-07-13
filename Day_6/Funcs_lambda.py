# def square(num):
#     return num ** 2

# print(square(5)) 

def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]

word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(word): 
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
