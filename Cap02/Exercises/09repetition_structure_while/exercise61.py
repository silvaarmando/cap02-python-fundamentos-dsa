# Create a program that reads two values ​​and shows a menu like the one below on the screen:

# [1] Add
# [2] Multiply
# [3] Larger
# [4] New numbers
# [5] Exit the program

# Your program must perform a requested operation in each case.
from time import sleep

value1 = int(input('First value: '))
value2 = int(input('Second value: '))
option = 0

while option != 5:
  print('''  [1] Add
  [2] Multiply
  [3] Larger
  [4] New numbers
  [5] Exit the program
  ''')
  option = int(input('>>>>> What is your option? '))
  if option == 1:
    print(f'The sum between {value1} and {value2} is {value1 + value2} ')
  elif option == 2:
    print(f'The product between {value1} x {value2} is {value1 * value2}')
  elif option == 3:
    if value1 > value2:
      larger = value1
    else:
      larger = value2
    print(f'Between {value1} and {value2} the highest value is {larger}.')
  elif option == 4:
    print('Enter the numbers again: ')
    value1 = int(input('First value: '))
    value2 = int(input('Second value: '))
  elif option == 5:
    print('Finishing...')
  else:
    print('Invalid option. Try again:')
  print('=-=' * 10)
  sleep(2)
  print('End of program! Check back often!')
