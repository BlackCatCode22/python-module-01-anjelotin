# Angelo Andrade
# 08-23-2024
# gross_pay.py

# Prompt
# This program will prompt the user for weekly hours worked and their hourly rate,
# then will compute and output gross pay. Bonus if you can handle overtime (hours worked
# over 40 hours will be paid at time and a half)

# Create prompt
name = input("Please enter your name:")
print("Hello, " + name + " this is a Gross Pay Program")

# Weekly hours worked
hours_worked = input("Please enter your hours worked:")
print(name + ", you worked " + hours_worked + " hours this week.")

# Hourly rate
hourly_rate = input("Please enter your hourly rate:")
print(name + " your hourly rate is " + hourly_rate + " an hour")


# Compute weekly pay
# convert stings to int
weekly_pay = int(hours_worked) * int(hourly_rate)
print(name + ", you earned $", weekly_pay, "this week.")

