produto = float(input('Qual o preço do produto: R$ '))
desconto = produto - (5 * produto / 100)
print(f'O produto que custava R$ {produto:.2f} na promoção \ncom desconto de 5% vai custar R$ {desconto:.2f}')