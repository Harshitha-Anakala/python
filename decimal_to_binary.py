a = int(input())
def decimal_to_binary(a):
    b = 0
    c = 1 
    if a==0:
        return 0
    else: 
         return (a % 2) + decimal_to_binary(a // 2) * 10
print(f" {decimal_to_binary(a)}")
