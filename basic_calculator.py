first_number=(int(input("enter 1st Number")))
second_number=(int(input("enter 2nd Number")))
operator=input("Choose operator'+', '-' , '*', '/', '%': ") 
if operator=='+':
    print((int(first_number ))+(int(second_number)))
elif operator=='-':
    print(int(first_number)-int(second_number))   
elif operator=='*':
    print(int(first_number)*int(second_number))
elif operator=='/':
    print(int(first_number)/int(second_number))
elif operator=='%':
    print(int(first_number)%int(second_number))
else:
    print('invalid operator')
  
    