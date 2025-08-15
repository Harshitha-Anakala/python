month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

if month == 1:
    number_of_days = 31
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        number_of_days = 29 
    else:
        number_of_days = 28
elif month == 3:
    number_of_days = 31
elif month == 4:
    number_of_days = 30
elif month == 5:
    number_of_days = 31
elif month == 6:
    number_of_days = 30
elif month == 7:
    number_of_days = 31
elif month == 8:
    number_of_days = 31
elif month == 9:
    number_of_days = 30
elif month == 10:
    number_of_days = 31
elif month == 11:
    number_of_days = 30
elif month == 12:
    number_of_days = 31
else:
    number_of_days = None
    print("Invalid month")

if number_of_days:
    print(f"{number_of_days} days.")



# #m=int(input())
# #y=int(input())
# #if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
#  #   days=31
#   #  print(f"this month has {days} days are present")
# #elif(m==4 or m==6 or m==9 or m==11):
#  #   days=30
#  #   print(f"this month has {days} days are present")
# #elif(m==2):
#        if(y%4==0 and y%100!=0) or (y%400==0):
#          days=29
#          print(f"this leap year, this months has {ly} days are present")
#        else:
#             days=28
#             print(f"this month has {days} days are present")
# else:
#     print("Invalid month")