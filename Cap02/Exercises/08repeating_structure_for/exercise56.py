from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1, 8):
  nasc = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
  idade = atual - nasc
  if idade >= 21:
    totmaior += 1
  else:
    totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoa maiores de idade\nE também tivemos {totmenor} pessoas menores de idade.')
