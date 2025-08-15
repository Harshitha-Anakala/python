name = input()
def count_vowels_consonants(name):
    vowels = " a,e,i,o,u,A,E,I,O,U"
    vowel_count = 0
    consonant_count = 0
    for char in name:
        if char.isalpha(): 
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count
print(count_vowels_consonants(name))
