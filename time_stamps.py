from datetime import datetime

# current date and time
now = datetime.now()

timestamp = datetime.strftime(now,"%d-%b-%Y  %a ")
print("timestamp =", timestamp)