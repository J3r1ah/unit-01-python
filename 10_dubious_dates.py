"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

from datetime import datetime #imports datetime
 
dt = datetime.now() #variable saying to make the datetime the current date and time using .now

print(dt)#printing it


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%m/%d/%Y")
current_time = current_datetime.strftime("%I:%M:%S %p")
print(f"Date: {formatted_date}, Time: {current_time}")

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
print("----task3----")
date_change1= "2023-10-01"
date_change2 = "2023-10-15"

date1 = datetime.strptime(date_change1, "%Y-%m-%d")
date2 = datetime.strptime(date_change2, "%Y-%m-%d")

difference = date2 - date1
print(f"The difference in days is: {difference.days}")

"""
Exercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print("----task4----")
print()
print()
birthdate = datetime.strptime(input("Enter your birthdate (YYYY-MM-DD): "), "%Y-%m-%d")
age = datetime.today().year - birthdate.year - (datetime.today() < birthdate.replace(year=datetime.today().year))
print(f"Your current age is: {age}")






