m = int(input("Enter the start number: "))
n = int(input("Enter the end number: "))

for i in range(m, n+1):
    a = i // 10  
    b = i % 10   
    c = a + b    
    print(c)     
