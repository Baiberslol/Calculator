import time
import os
import sys
import ctypes
#-------------------------------------------------------------------------------
if os.name == "nt":  # If the system is windows
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Python Calculator - Made by Terium#9139 on discord")
#-------------------------------------------------------------------------------

license = "-This project made by 'Terium#9139' on discord / 'Baiberslol' on github. DO NOT skid this tool."
license2 = "-If you like it you can rate it at github :) 'https://Github.com/Baiberslol'"
print(license,"\n", license2)
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')
#-------------------------------------------------------------------------------
from subprocess import call
call('color b', shell=True)
#--------------------------------------------------------------------------------

print("""
  :'######:::::'###::::'##::::::::'######::'##::::'##:'##::::::::::'###::::'########::'#######::'########::
'##... ##:::'## ##::: ##:::::::'##... ##: ##:::: ##: ##:::::::::'## ##:::... ##..::'##.... ##: ##.... ##:
 ##:::..:::'##:. ##:: ##::::::: ##:::..:: ##:::: ##: ##::::::::'##:. ##::::: ##:::: ##:::: ##: ##:::: ##:
 ##:::::::'##:::. ##: ##::::::: ##::::::: ##:::: ##: ##:::::::'##:::. ##:::: ##:::: ##:::: ##: ########::
 ##::::::: #########: ##::::::: ##::::::: ##:::: ##: ##::::::: #########:::: ##:::: ##:::: ##: ##.. ##:::
 ##::: ##: ##.... ##: ##::::::: ##::: ##: ##:::: ##: ##::::::: ##.... ##:::: ##:::: ##:::: ##: ##::. ##::
. ######:: ##:::: ##: ########:. ######::. #######:: ########: ##:::: ##:::: ##::::. #######:: ##:::. ##:
:......:::..:::::..::........:::......::::.......:::........::..:::::..:::::..::::::.......:::..:::::..::\n""" )

time.sleep(0.5)


def add(x, y):
    return x + y

def substract (x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("[*] 1.Add +")
print("[*] 2.Substract -")
print("[*] 3.Multiply *")
print("[*] 4.Divide /")

while True:
    choice = input("Enter choice (1-2-3-4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            
        elif choice == '2':
            print(num1, "-", num2, "=", substract(num1, num2))
            
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
            
            
    next_calculation = input("Lets do another calculation? (yes/no): ")
    if next_calculation == "no":
        print("See you next time! :)")
        time.sleep(2)
        break
    
    else: ("invalid input")
