def calculate(first_number, second_number, operator):

  if operator == '+':
    return first_number + second_number
  elif operator == '-':
    return first_number - second_number
  elif operator == '*':
    return first_number * second_number
  elif operator == '/':
    if second_number == 0:
      raise ZeroDivisionError("Division by zero is not allowed.")
    return first_number / second_number
  elif operator == '%':
    return first_number % second_number
  else:
    raise ValueError("Invalid operator. Please use +, -, *, /, or %.")

while True:
  first_number = int(input("Enter 1st number: "))
  second_number = int(input("Enter 2nd number: "))
  operator = input("Choose operator (+, -, *, /, %): ")

  try:
    result = calculate(first_number, second_number, operator)
    print(f"The result is: {result}")
  except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

  continue_program = input("Do you want to continue? (y/n): ")
  if continue_program.lower() != 'y':
    break

print("Thank you for using the calculator!")
