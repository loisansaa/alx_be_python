size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
  for column in range(size):
    print("*", end="")
  print()  # Move to the next line after printing a row
  row += 1