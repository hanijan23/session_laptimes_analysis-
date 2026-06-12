import json
from operator import itemgetter

def get_best_session_times(data, session): #returns a dictionary of best times of drivers depending on their qualified place, q1, q2, or q3
    best_times = {}

    for y in range(len(data["drv"])):

        if data["qs"][y] != session:
            continue

        if data["time"][y] == "None":
            continue

        sort_driver = data["drv"][y]
        sort_time = data["time"][y]
        sort_time = float(sort_time)

        if sort_driver not in best_times:
            best_times[sort_driver] = sort_time
        elif best_times[sort_driver] > sort_time:
            best_times[sort_driver] = sort_time
    
    return best_times

def main():

    try:
        with open("session_laptimes.json", "r") as json_file: #open and reads the json file
            data = json.load(json_file)

    except FileNotFoundError:
        print("Error: JSON file not found. Check file path.")
        return
    
    list_of_drivers = []
    counter = 0
    for k in range(len(data["drv"])):
        if data["drv"][k] not in list_of_drivers:
            list_of_drivers.append(data["drv"][k])
            counter += 1

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
        print("Best Valid Q2: Unfortunately, the driver did not make it past Q1")
        print("Best Valid Q3: Unfortunately, the driver did not make it past Q1")
    elif len(driver_q3) == 0:
        smallest_q2 = min(driver_q2)
        print("Best Valid Q2: " + str(smallest_q2) + "s")
        print("Best Valid Q3: Unfortunately, the driver did not make it past Q2")
    else:
        smallest_q2 = min(driver_q2)
        smallest_q3 = min(driver_q3)
        print("Best Valid Q2: " + str(smallest_q2) + "s")
        print("Best Valid Q3: " + str(smallest_q3) + "s")
    print("--------------------------------------------------------------------------")
    
    q3_items = list(get_best_session_times(data, "Q3").items())
    q3_items.sort(key  = itemgetter(1))
    q3_drivers = []
    for driver in q3_items:
        q3_drivers.append(driver[0])

    q2_items = list(get_best_session_times(data, "Q2").items())
    q2_items.sort(key=itemgetter(1))
    q2_drivers = []
    for driver in q2_items:
        if driver[0] not in q3_drivers:
            q2_drivers.append(driver[0])

    q1_items = list(get_best_session_times(data, "Q1").items())
    q1_items.sort(key=itemgetter(1))
    q1_drivers=[]
    for driver in q1_items:
        if (driver[0] not in q2_drivers) and (driver[0] not in q3_drivers):
            q1_drivers.append(driver[0])

    driver_pos = q3_drivers + q2_drivers + q1_drivers
    position = driver_pos.index(user_driver) + 1

    print("\n")
    print("Upon the final classified qualifying position, your driver: " + str(user_driver) + " has been placed " + str(position) + " out of a total of " + str(counter) + " drivers.")
    print("\n")
    if position<10:
        print("Wow, your team has made it through to the Australian Grand Prix.")
    else:
        print("Unfortuntately, your team did not make it through to Q3 and won't be racing in the Australian Grand Prix")

    
if __name__ == "__main__":
    main()



        
