distancia = float(input('Qual é a distância da sua viagem? (200) '))
if (distancia < 200):
  print(f'Você está prestes a começar uma viagem de {distancia} Km.')
  preco = distancia * 0.50
  print(f'E o preço da sua passagem será de R$ {preco:.2f}.')
else:
  print(f'Você está prestes a começar uma viagem de {distancia} Km.')
  preco = distancia * 0.45
  print(f'E o preço da sua passagem será de R$ {preco:.2f}.')
