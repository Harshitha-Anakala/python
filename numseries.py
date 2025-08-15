n = int(input("Enter the number: "))
current_value = 0
for i in range(1, n + 1):
    if i % 2 == 0:  
        current_value = i * i - 2
    else:  
        current_value = i * i - 1
    
    print(current_value, end=" ")
