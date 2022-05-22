# Make a program that reads an integer and says whether or not it is a main number.

number = int(input('\033[35mType a number: '))
total = 0
for c in range(1, number + 1):
  if number % c == 0:
    print('\033[31m', end='')
    total += 1
  else:
    print('\033[33m', end='')
  print(f'{c}', end=' ')
print(f'\n\033[32mThe number {number} was divisible {total} times.')
if total == 2:
  print('\033[mAnd so it is a PRIME NUMBER.')
else:
  print('\033[mAnd so it is NOT A PRIME NUMBER.')

# Note: use the powershell or similar terminal if you want the colors on your cmd.
