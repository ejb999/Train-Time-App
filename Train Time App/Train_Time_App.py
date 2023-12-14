
# import tkinter as tk


# root = tk.Tk()
# root.title("Train Time Calculator")
# root.geometry("600x400+400+200")


# def retrieve_inputs():
#     input_maxspeed = s_entry.get()
#     input_maxacel = a_entry.get()
#     input_ds = [d1, d2, d3, d4, d5]
    
#     print(f"Max Speed: {input_maxspeed}")
#     print(f"Max Accel: {input_maxacel}")
#     print(f"distances: {input_ds}")

# def makegui():
    
#     def retrieve_inputs():
#         input_maxspeed = s_entry.get()
#         input_maxacel = a_entry.get()
#         input_ds = [d1, d2, d3, d4, d5]
    
#         print(f"Max Speed: {input_maxspeed}")
#         print(f"Max Accel: {input_maxacel}")
#         print(f"distances: {input_ds}")
    
#     label = tk.Label(root, text="Enter Max Speed: Km/H")
#     label.pack()

#     s_entry = tk.Entry(root, text="max speed")
#     s_entry.pack()

#     label = tk.Label(root, text="Enter Max Accel: M/S^2")
#     label.pack()
#     a_entry = tk.Entry(root)
#     a_entry.pack()

#     label = tk.Label(root, text="Enter Distances to Stations: KM")
#     label.pack()
#     d1 = tk.Entry(root)
#     d1.pack()
#     d2 = tk.Entry(root)
#     d2.pack()
#     d3 = tk.Entry(root)
#     d3.pack()
#     d4 = tk.Entry(root)
#     d4.pack()
#     d5 = tk.Entry(root)
#     d5.pack()
#     button = tk.Button(root, text="Calculate", command=retrieve_inputs)
#     button.pack()
    
# makegui()



# root.mainloop()

while True:

    print("")
    print("")
    print("----------------------------------------------------------------------------------------------------")

    # https://en.wikipedia.org/wiki/BVG_Class_F - Berlin Trains have 1.5mss
    # The current world speed record for a commercial train on steel wheels is held by the French TGV at 574.8 km/h (357.2 mph)
    print("Berlin Trains have 1.5mss")
    print("The current world speed record for a commercial train on steel wheels is held by the French TGV at 574.8 km/h (357.2 mph)    this is about 5.4 km/h/s. ")


    # Input parameters
    max_acceleration = float(input("Enter maximum acceleration (m/s^2): "))
    max_speed = ((float(input("Enter maximum speed (km/h): ")))*1000)/3600
    number_of_stations = int(input("Enter the number of stations: "))
    station_names = []
    
    for i in range(number_of_stations):
        station_names.append(input(f"Name of Station {i}:  "))
    
    distances = [0]


    for i in range(number_of_stations - 1):
        distances.append((float(input(f"Enter the distance to station {i+1} (KM): ")))*1000)

    print(distances)

    def calculate_travel_time(max_acceleration, max_speed, distance_to_station):
        # Time to reach max speed
        t_max_speed = max_speed / max_acceleration

        # Distance covered during acceleration and deceleration
        d_accel = 0.5 * max_acceleration * t_max_speed ** 2
        d_decel = d_accel  # Assuming symmetric acceleration and deceleration
        d_accel_decel = d_accel + d_decel

        # Check if the train reaches max speed
        if d_accel_decel < distance_to_station:
            # Train reaches max speed
            # Time at constant speed
            d_const_speed = distance_to_station - d_accel_decel
            t_const_speed = d_const_speed / max_speed

            # Total time
            total_time = t_max_speed + t_const_speed + t_max_speed
        else:
            # Train does not reach max speed, adjust calculations
            new_max_speed = (2 * max_acceleration * (distance_to_station / 2)) ** 0.5
            t_accel_decel = new_max_speed / max_acceleration

            # Total time is twice the time to accelerate
            total_time = 2 * t_accel_decel
        
        return total_time / 60  # Convert to minutes


    # Loop to input distances and calculate times
    totaldistancetoend = 0
    totaltimetoend = 0
    temp = 0

    time_to_station = [calculate_travel_time(max_acceleration, max_speed, distance) for distance in distances]
    
    print(f"The times between stations {time_to_station}")
    print(station_names)
    
    for i in range(len(time_to_station)):
        temp += time_to_station[i]
        print(f"Time to station {i+1}: {station_names[i]} is: {temp}")
    
    
    # for i in range(number_of_stations - 1):
    #     print(distances[i+1])
    #     print(f"Time to reach station {i+1}: {time_to_station[i]} minutes")
        


    input("END OF PROGRAM - PRESS ENTER TO RESTART")


    def Inferingfigures():
        return()

