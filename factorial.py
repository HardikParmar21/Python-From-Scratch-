num=int(input("Enter the number you want to cheak :"))
factioral=1

if (num<0):
  print("factioral dos't exist")
elif (num==0):
    print("factioral of 0 is 1") 
else:
    i=num+1
    for i in range(i,num+1):
        factioral=  factioral*i
        print("factioral of ",num,"is ",factioral)     

