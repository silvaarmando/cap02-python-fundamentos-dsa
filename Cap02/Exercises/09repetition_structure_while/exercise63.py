print('Arithmetic Progression Generator with While')
print('_/\_' * 10)
first = int(input('First term: '))
reason = int(input('PA reason: '))
term = first
count = 1
while count <= 15:
  print(f'{term} -> ', end='')
  term += reason
  count += 1
print('END')
