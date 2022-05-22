a = int(input('First Number: '))
b = int(input('Second Number: '))
c = int(input('Third Number: '))

# Verificando o menor número...
menor = a
if b < a and b < c:
  menor = c
if c < a and c < b:
  menor = b 

# Verificando o maior número...
maior = a
if b > a and b > c:
  maior = b 
if c > a and c > b:
  maior = c 
print(f'The lowest number is {menor}.')
print(f'The higher number is {maior}.')
