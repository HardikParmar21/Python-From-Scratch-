person1_name = input("enter first person full name :")
person2_name = input("enter second person full name :")

last_name1 = person1_name.split()[-1]
last_name2 = person2_name.split()[-1]

result="ARE BROTHERS" if last_name1==last_name2 else"NOT"

print(result)