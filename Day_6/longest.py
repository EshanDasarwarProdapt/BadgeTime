def longest_word(text):
    words = text.split()
    x = ""
    for word in words:
        if len(word) > len(x):
            x = word
    return x

x = input("Enter a sentence: ")
result = longest_word(x)
print(f"The longest word in the sentence is: {result}")