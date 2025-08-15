n = int(input("Enter a number: ")) 
for i in range(2, n+1):  
    prime = 1 
    for j in range(2, int(i**0.5) + 1):   
        if i % j == 0:  
            prime = 0
            break
    if prime == 1:
        print(i)  
