casa = float(input('Qual o valor do imóvel: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
if (casa / (anos * 12)) <= (salario - (salario * 40 / 100)):
    print(f'Para financiar uma casa no valor de R$ {casa:.2f} em {anos} anos a parcela ficaria {casa / (anos * 12):.2f} R$ mensais.\nEMPRESTIMO APROVADO.')
else:
    print(f'Para financiar uma casa no valor de R$ {casa:.2f} em {anos} anos a parcela ficaria {casa / (anos * 12):.2f} R$ mensais.\nEMPRESTIMO NEGADO.')