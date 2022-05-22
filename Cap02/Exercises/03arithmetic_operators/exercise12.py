largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2 # Para pintar uma parede serão necessários 2 litros de tinta
print(f'Sua parede tem a dimensão de {largura} x {altura} e possuí uma área de {area} m². \nPara pintar essa parede você precisará de {tinta} l de tinta.')