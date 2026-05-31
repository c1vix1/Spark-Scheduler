import os
import json

debug = True
exit = False

with open("welcome.txt", "r", encoding="utf-8") as file:
    print(file.read())

try:
    # Query standard output descriptor
    terminalColumns, terminalLines = os.get_terminal_size()
    if debug == True:
        print(f"Terminal width: {terminalColumns}")
except OSError:
    print("Not running in a standard terminal viewport.")
    terminalColumns = 10 
for i in range(terminalColumns):
    print("-",end="")

if terminalLines <= 30 and debug == False:
    print("Terminal Too Small. Please Raise Terminal Size")
    exit = True

while exit != True:
    print("Hello")
    exitResponce = input("Exit?(Y/N)").lower()
    if exitResponce == "y" or exitResponce == "yes":
        exit = True
    else:
        exit = False
print("Exited")