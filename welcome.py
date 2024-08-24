# Angelo Andrade
# 8-23-2023
# welcome.py

# This program uses input to prompt a user for their name and then welcomes them. 
# Bonus if you can get the system time and then adjust your greeting to "Good morning,
# good afternoon, or good evening.

# Getting the system time
import time


# Create prompt for user
name = input("Please enter your name: ")
print("Hello, " + name + " it's a pleasure meeting you!")

# Current time system time
current_time = time.strftime("%H:%M:%S", time.localtime())
current_hour = int(time.strftime("%H"))
print("the current time is:", current_time)

# Good morning Greeting (5am - 12pm)
if current_hour >= 5 and current_hour < 12:
    print("GOOD MORNING!", name + " have a nice day.")
# Good afternoon (12pm - 5pm)
elif current_hour >= 12 and current_hour < 17:
    print("GOOD AFTERNOON!", name + " have a nice rest of your day.")
# Good evening (5pm - 9pm)
elif current_hour >= 17 and current_hour < 21:
    print("GOOD EVENING! " + name + " have a nice evening.")
# Good night (9pm - 5am)
else:
    print("GOOD NIGHT, " + name)

