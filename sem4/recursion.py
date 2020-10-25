#programm by 00009734

from os import system, name
from time import sleep

#to clear cmd
def clear():
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

#Counts from positive number to 0
def recursionDown(number):
    if number > 0:
        print(number)
        sleep(0.3)
        recursionDown(number-1)

#Counts from negative number upto 0
def recursionUp(number):
    if number < 0:
        print(number)        
        sleep(0.3)
        recursionUp(number+1)

while True:
    print("Programm will count until zero from your number")
    number = int(input("Write your number: "))

    if number > 0:
        recursionDown(number)
    elif number < 0:
        recursionUp(number)
    else:
        i = input("Nothing to count, it's 0\nTry again")
        clear()
        continue

    print(0)
    print("\n\tGame over")
    i = input('Press "Enter" to restart game')
    clear()