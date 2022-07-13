import time
import os
import sys
import ctypes


if os.name == "nt":  # If the system is windows
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Python Calculator - Made by Terium#9139 on discord")


from subprocess import call

call('color b', shell=True)

print("""
  #####                                                                         
 #     #    ##    #        ####   #    #  #         ##    #####   ####   #####  
 #         #  #   #       #    #  #    #  #        #  #     #    #    #  #    # 
 #        #    #  #       #       #    #  #       #    #    #    #    #  #    # 
 #        ######  #       #       #    #  #       ######    #    #    #  #####  
 #     #  #    #  #       #    #  #    #  #       #    #    #    #    #  #   #  
  #####   #    #  ######   ####    ####   ######  #    #    #     ####   #    #\n""" )

time.sleep(0.5)

output_file = "Calculation-log.txt"


def add(x, y):
    return x + y

def substract (x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            
        elif choice == '2':
            print(num1, "-", num2, "=", substract(num1, num2))
            
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
            
            
    next_calculation = input("Lets do next calculation? (yes/no): ")
    if next_calculation == "no":
        print("See you next time!")
        time.sleep(2)
        break
    
    else: ("invalid input")