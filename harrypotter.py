
num = int(input("Enter the four digit number: "))
num =abs(num)
first_digit= num//1000
last_digit= num % 10
sum = first_digit + last_digit
print(sum)