#!/usr/bin/python

"""
Write code that asks the user to enter their birthday in the form mm/dd/yyyy,
and then prints a string of the form 'You were born in the year yyyy'
"""

dateBirthday = input("Enter a birthday in format mm/dd/yyyy :")

#print(dateBirthday)

birthday = dateBirthday.split('/')

print(f"You were born in the year {birthday[2]}")
