import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = (int(time.strftime('%H'))) 
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

current_time = time.time()
if current_time<12:
    print("Good Morning")
elif current_time<18:
    print("Good Afternoon")
else:
    print("Good Evening")              