# Author: Jai
import calendar
import os
import turtle

print()
print('''hey you standing in the cold,
getting lonely, getting old,
can you feel me?''')
print()
print("hell yeah!")
print()
# os module
print(os.listdir())
# playsound('C:\\Users\\Jai\\Documents\\python\\play.mp3')
print()
# turle module
'''jai = turtle.Turtle()
for i in range(4):
    jai.forward(100)
    jai.right(90)'''

'''def square():
    for i in range(4):
        jai.forward(100)
        jai.right(90)


square()
jai.forward(100)
square()

turtle.done()'''

# Calender module
print(calendar.weekheader(3))
print()
print(calendar.month(2020, 10))

# variables in python
age = 10
price = 19.95
first_name = 'Jai'
is_online = True

# input from CL
name = input("What is you name? ")
print("Hello " + name)
print()

# Type conversion
birth_year = input("What is you birth year: ")
age = 2020 - int(birth_year)
print(age)
'''int() float() bool()'''
