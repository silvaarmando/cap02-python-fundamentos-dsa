from random import randint

itens = (
  'PEDRA',
  'PAPEL',
  'TESOURA'
)

computador = randint(0, 2)
print('=-*-=' * 7)
print('*         JO! KEN! PO!            *')
print('''*                                 *
*         SUAS OPÇÕES:            *
*                                 *
*         [ 0 ] PEDRA             *
*         [ 1 ] PAPEL             *
*         [ 2 ] TESOURA           *
*                                 *''')
jogador = int(input('*      QUAL É A SUA JOGADA? '))
print('=-*-=' * 7)
print(f'*   O Computador escolheu {itens[computador]}   *')
print(f'*      O Jogador jogou {itens[jogador]}      *')

# Computador jogou PEDRA
if computador == 0:
  if jogador == 0:
    print('*            EMPATE!              *')
  elif jogador == 1:
    print('*        JOGADOR VENCEU!          *')
  elif jogador == 2:
    print('*      COMPUTADOR VENCEU!         *')
  else:
    print('* JOGADA INVÁLIDA! TENTE NOVAMENTE*')

# Computador jogou PAPEL
elif computador == 1:
  if jogador == 0:
    print('*      COMPUTADOR VENCEU!         *')
  elif jogador == 1:
    print('*           EMPATE!               *')
  elif jogador == 2:
    print('*        JOGADOR VENCEU!          *')
  else:
    print('* JOGADA INVÁLIDA! TENTE NOVAMENTE*')

# Computador jogou TESOURA
elif computador == 2:
  if jogador == 0:
    print('*         JOGADOR VENCEU!         *')
  elif jogador == 1:
    print('*       COMPUTADOR VENCEU!        *')
  elif jogador == 2:
    print('*            EMPATE!!             *')
  else:
    print('* JOGADA INVÁLIDA! TENTE NOVAMENTE*')
else:
  print('* JOGADA INVÁLIDA! TENTE NOVAMENTE*')
print('=-*-=' * 7)
