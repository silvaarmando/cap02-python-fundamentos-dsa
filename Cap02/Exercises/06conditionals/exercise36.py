lado1 = float(input('Primeiro Lado: '))
lado2 = float(input('Segundo Lado: '))
lado3 = float(input('Terceiro Lado: '))
if lado1 < lado2 + lado3 and lado2 < lado3 + lado1 and lado3 < lado1 + lado2:
  print('Os lados acima PODEM FORMAR Triângulo.')
else:
  print('Os lados acima NÃO PODEM FORMAR Triângulo.')
