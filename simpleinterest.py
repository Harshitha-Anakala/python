principle_amount = float(input("enter the principle amount: "))
rate_of_interest = float(input("enter the interest: "))
num_of_years = float(input("enter the number of years: "))
simple_interest = (principle_amount * rate_of_interest * num_of_years) //100
total_amount= principle_amount + simple_interest
discount= simple_interest* 0.02
final_amount= total_amount- discount
print(simple_interest)
print(total_amount)
print(discount)
print(final_amount)