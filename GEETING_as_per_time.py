Time=int(input("Whats the current time as per 24 hour system : "))
if(Time >= 5 and Time < 12):
    print("Good Morning!!!")
elif(Time>=12 and Time<=16):
    print("Good Afternoon!!!")
elif(Time>=17 and Time<=24):
    print("Good Evening!!!")
elif(Time>=0 and Time<4):
    print("Time to go to bed!!!")
else:
    print("Worng time!")
    
            
