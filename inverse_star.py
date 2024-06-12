rows = 5  # Number of rows in the pattern


i=1

while i<=7:
    print(i*'*')
    i=i+1
i = rows
while i > 0:
  # Print spaces before stars based on row number
  j = 1
  while j <= rows - i:
    print(" ", end="")
    j += 1
  # Print stars based on remaining spaces
  j = 1
  while j <= 2 * i - 1:
    print("*", end="")
    j += 1
  print()  # Move to the next line after each row
  i -= 1
