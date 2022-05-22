from math import hypot

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
print(f'A hipotenusa vai medir {hypot(co, ca):.2f}.')