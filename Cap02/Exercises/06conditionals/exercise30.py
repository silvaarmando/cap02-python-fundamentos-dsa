velocidade = float(input('Qual a velocidade atual do carro? '))
if (velocidade > 80.0):
  print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
  multa = (velocidade - 80) * 7
  print(f'Você deve pagar uma multa de R$ {multa:.2f}')
print(f'Tenha um bom dia! Dirija com SEGURANÇA!')
