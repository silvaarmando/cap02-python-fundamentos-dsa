# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

res = 'S'
soma = quant = media = maior = menor = 0
while res in 'Ss':
  number = int(input('Digite um número: '))
  soma += number
  quant += 1

  res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}')
