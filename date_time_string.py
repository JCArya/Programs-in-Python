
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("Year:", year)

month = now.strftime("%B")
print("Month:", month)

day = now.strftime("%d")
print("Day:", day)

weekday = now.strftime("%A")
print("Weekday:", weekday)

time = now.strftime("%H:%M:%S")
print("Time:", time)

date_time = now.strftime("%d-%B-%Y,%A, %I:%M:%p")
print("Date And Time:",date_time)