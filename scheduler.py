import os
import json
import sqlite3

debug = True
exit = False

con = sqlite3.connect("app_data.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS events(name TEXT NOT NULL,type INTEGER NOT NULL,length FLOAT NOT NULL,preferedTime TIME,setTimeStart TIME,setTimeEnd TIME)")

with open("welcome.txt", "r", encoding="utf-8") as file:
    print(file.read())

try:
    terminalColumns, terminalLines = os.get_terminal_size()
    if debug == True:
        print(f"Terminal width: {terminalColumns}")
except OSError:
    print("Not running in a standard terminal viewport.")
    terminalColumns = 10 
for i in range(terminalColumns):
    print("-",end="")

if terminalLines <= 15 and debug == False:
    print("Terminal Too Small. Please Raise Terminal Size")
    exit = True

while exit != True:
    numberOfEvents = input("Total Events")
    for i in range(numberOfEvents):
        eventName = input("Event Name")

print("Exited")