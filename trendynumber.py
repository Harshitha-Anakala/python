num = int(input("Enter a number: "))
if 100 <= num <= 999:
    digit= num//10
    middle_digit = digit % 10
    if middle_digit % 3 == 0:
        print("Trendy Number")
    else:
        print("Invalid Number")
else:
    print("Invalid Number")
