# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quando números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

number = count = soma = 0
number = int(input('Digite um número [999 para parar]: '))
while number != 999:
  soma += number
  count += 1
  number = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {count} e a soma entre eles foi {soma}.')
