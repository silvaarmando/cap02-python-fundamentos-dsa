from random import randint
from time import sleep
from emoji import emojize

print('>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<')
print('         VOU PENSAR EM UM NÚMERO DE 0 A 5. TENTE ADIVINHAR              ')
print('>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<>-><-<')

numero = int(input('Em que número eu pensei? '))
lista =[ 0, 1, 2, 3, 4, 5 ]
pensei = randint(0, 5) # Faz o computador pensar...
sleep(1.5)
print('PROCESSANDO...')
sleep(1.5)
if (numero == pensei):
  print('PARABÉNS! Você conseguiu me vencer!')
  print(emojize(':stuck_out_tongue_winking_eye:',use_aliases = True))
  sleep(1.5)
else:
  print(f'GANHEI! Eu pensei no número {pensei} e não no número {numero}')
  print(emojize(':scream:',use_aliases = True))
  sleep(1.5)