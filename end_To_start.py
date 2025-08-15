"""words = input().split()
def check_sequence(words):
    for i in range(len(words) - 1):
        if words[i][-1].lower() != words[i + 1][0].lower():
            return  
    print("The sequence is valid.")
check_sequence(words)"""

str = input()
b = "####" 
a = " "  
while str != b:
    if a == " " or a[-1] == str[0]:  
        print(str)  
        a = str  
        str = input()  
    else:
        break  