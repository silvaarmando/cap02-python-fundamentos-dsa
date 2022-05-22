dias = int(input('Por quantos dias o carro foi alugado? '))
quilo = float(input('Quantos quilometros rodados? '))
preco = (dias * 60) + (quilo * 0.15)
print(f'O total a pagar pelo aluguel do carro é R$ {preco}')