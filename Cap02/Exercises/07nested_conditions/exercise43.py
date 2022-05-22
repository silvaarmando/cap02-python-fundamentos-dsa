from datetime import date

ano_atual = date.today().year
nascimento = int(input('Ano de NASCIMENTO: '))
idade = ano_atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print(f'IDADE: {idade} anos. \nClassificação: MIRIM.')
elif idade <= 14:
    print(f'IDADE: {idade} anos. \nClassificação: INFANTIL.')
elif idade <= 19:
    print(f'IDADE: {idade} anos. \nClassificação: JÚNIOR.')
elif idade <= 25:
    print(f'IDADE: {idade} anos. \nClassificação: SÊNIOR.')
else:
    print(f'IDADE: {idade} anos. \nClassificação: MASTER.')