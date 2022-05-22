# Escreva um programa que leia um número n inteiro qualquee mostre na tela os n primeiros elementos de uma Sequência de Fibonacci

print('-|-' * 15)
print('            Sequência de Fibonacci')
print('-|-' * 15)
print('')

number = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('-~~-' * 15)
print(f'{t1} -> {t2}', end='')
count = 3
while count <= number:
  t3 = t1 + t2
  print(f' -> {t3}', end='')
  t1 = t2
  t2 = t3
  count += 1
print(' -> FIM')
print('-~~-' * 15)
