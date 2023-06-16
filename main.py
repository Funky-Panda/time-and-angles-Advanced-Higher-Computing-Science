import datetime

time = (datetime.datetime.now() + datetime.timedelta(hours=1)).time()
hour = time.strftime("%I")
minute = time.strftime("%M")
print("Current Time: " + str(time)[:5])

minute_degrees = int(minute) * 6
hour_degrees = int(hour)* 30 + (int(minute) / 60) * 30

if hour_degrees == 360:
    print(f"Hour: 0/{hour_degrees}°")
else:
    print(f"Hour: {hour_degrees}°")

if minute_degrees == 0:
    print(f"Minute: 0/360°")
else:
    print(f"Minute: {minute_degrees}°")