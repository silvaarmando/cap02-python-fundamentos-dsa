'''
Equilátero: todos os lados iguais.
Isósceles: dois lados iguais.
Escaleno: todos os lados diferentes.
'''

l1 = float(input('Primeiro Lado: '))
l2 = float(input('Segundo Lado: '))
l3 = float(input('Terceiro Lado: '))
if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l3:
    print('Os lados acima podem formar um triângulo ', end='')
    if l1 == l2 == l3: 
        print('EQUILÁTERO!')
    elif l1 != l2 != l3:
        print('ESCALENO!')
    else: 
        print('ISÓSCELES')
else:
    print('Os lados acima NÃO PODEM FORMAR um triângulo')