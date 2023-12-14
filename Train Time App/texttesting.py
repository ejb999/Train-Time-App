# Input parameters
max_acceleration = float(input("Enter maximum acceleration (m/s^2): "))
max_speed = float(input("Enter maximum speed (m/s): "))
number_of_stations = int(input("Enter the number of stations: "))

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



# Loop to input distances and calculate times
for i in range(number_of_stations):
    distance = float(input(f"Enter the distance to station {i+1} (meters): "))
    time_to_station = calculate_travel_time(max_acceleration, max_speed, distance)
    print(f"Time to reach station {i+1}: {time_to_station:.2f} minutes")