"""
Your Task
Build an application that:
1. Reads the JSON dataset from a local file path
2. Takes user input to specify a driver (e.g. HUL, BOR)
3. Presents the selected driver’s:
a. Best valid lap time from each of the three sessions (Q1, Q2, Q3)
b. Final classified qualifying position based upon the dataset
"""

import json

with open("session_laptimes.json", "r") as json_file:
    data = json.load(json_file)                             #this reads the JSON file

print(len(data))
print(type(data)) #found out this is a dict
print(data.keys())
print(data["drv"][10:40])
print(data["lap"][:5])

#print functions to understand the json file...

#the goal is to compare lap times. From the spec, use sesT, units seconds

print(data["sesT"][:10]) #shows lap times in seconds

driver = input("Please specify a driver in 3 letters: ")

driver_laps = []

for i in range(len(data["drv"])):
    if data["drv"][i] == driver:
        driver_laps.append(data["sesT"][i])

print(driver_laps)

print(data["s2"][:5])
print(data["qs"][:50])
print(data["time"][:5])

#the important variables are drv, qs, sesT

list_of_drivers = []
counter = 0
for k in range(len(data["drv"])):
    if data["drv"][k] not in list_of_drivers:
        list_of_drivers.append(data["drv"][k])
        counter += 1
print(list_of_drivers, counter) #shows how many indivdual teams are competing

test_driver = "HUL"

for j in range(len(data["drv"])):
    if data["drv"][j] == test_driver:
        print(data["qs"][j], data["sesT"][j])





