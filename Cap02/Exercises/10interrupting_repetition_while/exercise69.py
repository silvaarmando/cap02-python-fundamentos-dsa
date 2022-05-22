while True:
  number = int(input('Quer ver a tabuada de qual valor? '))
  print('-*-' * 15)
  if number < 0:
    break
  for c in range(1, 11):
    print(f'{number} x {c} = {number * c}')
  print('-*-' * 15)
print('PROGRAMA TABUADA ENCERRADO!')
