'''
Medidas:

Abaixo de 18.5: Abaixo do peso.
Entre 18.5 e 25: Peso ideal.
25 até 30: Sobrepeso.
30 até 40: Obesidade.
Acima de 40: Obesidade mórbida. 
'''

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O imc dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE.')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
else: 
    print('Acho que você digitou algo errado!!!')