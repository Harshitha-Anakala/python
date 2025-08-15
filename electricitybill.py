units_consumed = int(input("Enter the units consumed: "))
if units_consumed <= 200:
    cost_per_unit = 0.5
    electricity_bill = units_consumed * cost_per_unit
elif units_consumed <= 400:
    cost_per_unit = 0.625
    electricity_bill = units_consumed*0.625+100
elif units_consumed <= 600:
    cost_per_unit = 0.80
    electricity_bill = units_consumed*0.80+200
elif units_consumed > 600:
    cost_per_unit = 1.25
    electricity_bill = units_consumed*1.25+425

print("Electricity Bill: Rs", electricity_bill)


    