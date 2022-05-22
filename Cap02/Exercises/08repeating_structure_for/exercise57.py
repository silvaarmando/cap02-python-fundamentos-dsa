major = 0
minor = 0

for w in range(1, 6):
  weight = float(input(f'{w}st person weight: '))
  if w == 1:
    major = weight
    minor = weight
  else:
    if weight > major:
      major = weight
    if weight < minor:
      minor = weight
print(f'The highest weight read was {major} Kg.')
print(f'The lowest weight read was {minor} Kg.')