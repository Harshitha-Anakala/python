number_of_hours_worked_Su = int(input())
number_of_hours_worked_M = int(input())
number_of_hours_worked_T = int(input())
number_of_hours_worked_W = int(input())
number_of_hours_worked_Th = int(input())
number_of_hours_worked_F = int(input())
number_of_hours_worked_S = int(input())

salary = 0

if number_of_hours_worked_M > 8:
    salary += (number_of_hours_worked_M * 100) + ((number_of_hours_worked_M - 8) * 15)
else:
    salary += number_of_hours_worked_M * 100
if number_of_hours_worked_T > 8:
    salary += (number_of_hours_worked_T * 100) + ((number_of_hours_worked_T - 8) * 15)
else:
    salary += number_of_hours_worked_T * 100

if number_of_hours_worked_W > 8:
    salary += (number_of_hours_worked_W* 100) + ((number_of_hours_worked_W - 8) * 15)
else:
    salary += number_of_hours_worked_W * 100

if number_of_hours_worked_Th > 8:
    salary += (number_of_hours_worked_Th * 100) + ((number_of_hours_worked_Th - 8) * 15)
else:
    salary += number_of_hours_worked_Th * 100

if number_of_hours_worked_F > 8:
    salary += (number_of_hours_worked_F* 100) + ((number_of_hours_worked_F - 8) * 15)
else:
    salary += number_of_hours_worked_F * 100

salary += number_of_hours_worked_S * (100 + 100 * 0.25)

salary += number_of_hours_worked_Su * (100 + 100 * 0.50)


print(f"Total salary: ₹{salary}")
