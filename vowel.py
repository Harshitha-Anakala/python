b = input("Enter the character: ")
v = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')  
if ((b>='a' and b<='z') or (b>='A' and b<='Z')):
    if b in v:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")


