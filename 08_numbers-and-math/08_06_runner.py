# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

# Convert time to hours
time_in_hours = (30 * 60 + 30) / 3600  # 30 minutes and 30 seconds to hours

# Calculate mph
mph_average_speed = 10 / time_in_hours  # miles per hour

# Convert mph to km/h
conversion_factor = 1.60934
kmh_average_speed = mph_average_speed * conversion_factor

# Print the average speed in km/h
print(kmh_average_speed)

