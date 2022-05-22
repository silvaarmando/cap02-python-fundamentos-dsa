number = int(input('Digite um número: '))
cont = 0
soma = 0
for c in range(1, number, 2):
  if c % 3 == 0:
    print(c, end=' ')
    soma = soma + c
    cont = cont + 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')