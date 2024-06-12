weight=float(input("enter your weight :"))
unit = input("(k)g or (l)bs: ")
if unit.upper=="k":
    convert =weight/0.45
    print("Your weight is :"+convert)
else:
    convert =weight*0.45
    print("Your weight is :"+str(convert))     
