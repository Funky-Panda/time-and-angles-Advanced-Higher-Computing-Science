# 1min = 6° , 1hr = 30°

import datetime

time = (datetime.datetime.now() + datetime.timedelta(hours=1)).time() # This gets the current time in python and adds one hour for BST time
hour = time.strftime("%I")
minute = time.strftime("%M")

minute_degrees = int(minute) * 6
hour_degrees = int(hour)* 30 + (int(minute) / 60) * 30

# Displays the current time to the user along with the degrees of both the hour and minutes

print("Current Time: " + str(time)[:5]) 

if hour_degrees == 360:
    print(f"Hour: 0/{hour_degrees}°")
else:
    print(f"Hour: {hour_degrees}°")

if minute_degrees == 0:
    print("Minute: 0/360°")
else:
    print(f"Minute: {minute_degrees}°")