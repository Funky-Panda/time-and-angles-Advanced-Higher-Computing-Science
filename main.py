# 1min = 6° , 1hr = 30°
import datetime

time = (datetime.datetime.now() + datetime.timedelta(hours=1)).time()
hour = time.strftime("%I")
minute = time.strftime("%M")
print("Current Time: "+ str(time)[:5])

minuteDegress = int(minute) * 6
hourDegress = int(hour) * 30

if hourDegress == 360:
    print(f"Hour: 0/{hourDegress}°")
else:
    print(f"Hour: {hourDegress}°")

if minuteDegress == 0:
    print(f"Minute: 0/360°")
else:
    print(f"Minute: {minuteDegress}°")