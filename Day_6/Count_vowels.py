def count_vowels(string):
    # vowels = "aeiou"
    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    
    for char in string.lower():
        if char in vowels:
            
            vowels[char] += 1
    return vowels

sentence = input("Enter a sentence: ")

result = count_vowels(sentence)
print(f"The vowels in the sentence are: {result}")



