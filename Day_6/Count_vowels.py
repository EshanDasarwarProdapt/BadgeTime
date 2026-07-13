def count_vowels(string):
    vowels = "aeiouAEIOU"
    
    d = {}
    for char in string.lower():
        if char in vowels:
            
            d[char] = d.get(char, 0) + 1
    return d

sentence = input("Enter a sentence: ")

result = count_vowels(sentence)
print(f"The vowels in the sentence are: {result}")



