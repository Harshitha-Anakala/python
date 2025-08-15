fprice = int(input("Enter FlipKart price: "))
fdiscount = int(input("Enter FlipKart discount percentage: "))
fcharges = int(input("Enter FlipKart charges: "))

sprice = int(input("Enter Snapdeal price: "))
sdiscount = int(input("Enter Snapdeal discount percentage: "))
scharges = int(input("Enter Snapdeal charges: "))

aprice = int(input("Enter Amazon price: "))
adiscount = int(input("Enter Amazon discount percentage: "))
acharge = int(input("Enter Amazon charges: "))

f_lowest = fprice * (1 - fdiscount / 100) + fcharges
s_lowest = sprice * (1 - sdiscount / 100) + scharges
a_lowest = aprice * (1 - adiscount / 100) + acharge

print("In FlipKart: Rs", f_lowest)
print("In Snapdeal: Rs", s_lowest)
print("In Amazon: Rs", a_lowest)

if (f_lowest < s_lowest) and (f_lowest < a_lowest):
    print("Choose Flipkart")
elif (s_lowest < f_lowest) and (s_lowest < a_lowest):
    print("Choose Snapdeal")
else:
    print("Choose Amazon")

 

