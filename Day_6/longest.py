def longest_word(text):
    words = text.split()
    x = ""
    for word in words:
        if len(word) > len(x):
            x = word
    return x
    # y = max(words, key=len)
    # return y


# x = input("Enter a sentence: ")
# result = longest_word(x)
# print(f"The longest word in the sentence is: {result}")


import time

text  = input("Enter a sentence: ")
start_time = time.perf_counter() #high-resolution timer to measure execution time better than time.time()

result = longest_word(text)
print(f"Longest word: {result}")

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.6f} seconds")


