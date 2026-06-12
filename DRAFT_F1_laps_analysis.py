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
from operator import itemgetter

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

print(data["s2"][:5])
print(data["qs"][:50])
print(data["time"][:5])

list_of_drivers = []
counter = 0
for k in range(len(data["drv"])):
    if data["drv"][k] not in list_of_drivers:
        list_of_drivers.append(data["drv"][k])
        counter += 1
print(list_of_drivers, counter) #shows how many indivdual teams are competing

test_driver = "NOR"

for j in range(len(data["drv"])):
    if data["drv"][j] == test_driver:
        print(str(test_driver) + ": " +  str(data["qs"][j]) + "  lap: " + str(data["lap"][j]) + "  start time: " +  str(data["lST"][j]) + "    end time: " + str(data["sesT"][j]) + "    lap time: " + str(data["time"][j]) + "  status: " + str(data["status"][j]) + "    pos: " + str(data["pos"][j]))


print(data["s1"][:20])

# to complete 3 part a, variables needed: drv, qs, lap, time

print("\n")
print("--------------------------------------------------------------")
print("This application presents the best valid lap times of a driver")
print("--------------------------------------------------------------")
print("Here are the following drivers you can select!")
print("\n")
print(list_of_drivers)
print("\n")

answer = False
while answer == False:
    user_driver = input("Please specify a driver using a 3 Letter Code from the following list: ")
    user_driver = user_driver.upper()
    if user_driver in list_of_drivers:
        answer = True
    else:
        print("Invalid driver, try again!")

driver_q1 = []
driver_q2 = []
driver_q3 = []

for x in range(len(data["drv"])):
    if data["drv"][x] == user_driver and data["qs"][x] == "Q1" and data["time"][x] != "None":
        time = float(data["time"][x])
        driver_q1.append(time)
    elif data["drv"][x] == user_driver and data["qs"][x] == "Q2" and data["time"][x] != "None":
        time = float(data["time"][x])
        driver_q2.append(time)
    elif data["drv"][x] == user_driver and data["qs"][x] == "Q3" and data["time"][x] != "None":
            time = float(data["time"][x])
            driver_q3.append(time)

smallest_q1 = min(driver_q1)

print("--------------------------------------------------------------------------")
print("Best Valid Q1: " + str(smallest_q1) + "s")
if len(driver_q2) == 0 and len(driver_q3) == 0:
    print("Unfortunately, the driver did not make it past Q1")
elif len(driver_q3) == 0:
    smallest_q2 = min(driver_q2)
    print("Best Valid Q2: " + str(smallest_q2) + "s")
    print("Unfortunately, the driver did not make it past Q2")
else:
    smallest_q2 = min(driver_q2)
    smallest_q3 = min(driver_q3)
    print("Best Valid Q2: " + str(smallest_q2) + "s")
    print("Best Valid Q3: " + str(smallest_q3) + "s")
print("--------------------------------------------------------------------------")

#now to calculate the position

top_q1 = {}     #{driver: best_time}
top_q2 = {}
top_q3 = {}

for y in range(len(data["drv"])):
    sort_driver = data["drv"][y]
    sort_session = data["qs"][y]
    sort_time = data["time"][y]

    if sort_time == "None":
        continue

    sort_time = float(sort_time)

    if sort_session == "Q3":
        if sort_driver not in top_q3 and sort_time != "None":
            top_q3[sort_driver] = sort_time
        else:
            if top_q3[sort_driver] > sort_time:
                top_q3[sort_driver] = sort_time
    
    elif sort_session == "Q2":
        if sort_driver not in top_q2 and sort_time != "None":
            top_q2[sort_driver] = sort_time
        else:
            if top_q2[sort_driver] > sort_time:
                top_q2[sort_driver] = sort_time

    elif sort_session == "Q1":
        if sort_driver not in top_q1 and sort_time != "None":
            top_q1[sort_driver] = sort_time
        else:
            if top_q1[sort_driver] > sort_time:
                top_q1[sort_driver] = sort_time

print("\n")
print(top_q3)
print("\n")
print(top_q2)
print("\n")
print(top_q1)
print("\n")

#shows Q3 - 20, Q2 - 16, Q3 - 9

q3_items = list(top_q3.items())
print(q3_items)
q3_items.sort(key  = itemgetter(1))
q3_drivers = []
for driver in q3_items:
    q3_drivers.append(driver[0])
print(q3_drivers)
print("\n")

q2_items = list(top_q2.items())
print(q2_items)
q2_items.sort(key=itemgetter(1))
q2_drivers = []
for driver in q2_items:
    if driver[0] not in q3_drivers:
        q2_drivers.append(driver[0])
print(q2_drivers)
print("\n")

q1_items = list(top_q1.items())
print(q1_items)
q1_items.sort(key=itemgetter(1))
q1_drivers=[]
for driver in q1_items:
    if (driver[0] not in q2_drivers) and (driver[0] not in q3_drivers):
        q1_drivers.append(driver[0])
print(q1_drivers)
print("\n")

print("The final order of driver positions are: ")
driver_pos = q3_drivers + q2_drivers + q1_drivers
print(driver_pos)
print("\n")

#for part 3b


position = driver_pos.index(user_driver) + 1

print("Upon the final classfied qualifying position, your driver: " + str(user_driver) + " has been placed " + str(position) + " out of a total of " + str(counter) + " drivers.")
if position<10:
    print("Wow, your team has made it through to the Australian Grand Prix.")
else:
    print("Unfortuntately, your team did not make it through to Q3 and won't be racing in the Australian Grand Prix")


#next, implement try and except for file handling
#implement function for the dictionary instead of repeating the same code
