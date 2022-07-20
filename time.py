from datetime import datetime

now = datetime.now()

start_time = now.strftime("%H:%M:%S")
print("Start Time =", start_time)
a = range(100000000)
for i in a:
    pass
now2 = now = datetime.now()

end_time = now2.strftime("%H:%M:%S")
print("End Time =", end_time)
