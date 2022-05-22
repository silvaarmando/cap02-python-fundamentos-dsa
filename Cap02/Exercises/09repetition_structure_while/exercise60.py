# Improve the game of CHALLENGE 028 where the computer will "think" of a number between 0 and 10. Only now the player will try to guess until he gets it right, showing in the end how many guesses it took to win.

from random import randint
from time import sleep

computer = randint(0, 10)
print('Hi, i am your computer ...')
sleep(2)
print('I just thought of a number between 0 and 10 ...')
sleep(2)
print('Can you guess what it was?')
sleep(2)
right = False
hunches = 0
while not right:
  player = int(input('What is your guess? '))
  hunches += 1
  if player == computer:
    right = True
  else:
    if player < computer:
      print('More ... Try again: ')
    elif player > computer:
      print('Less ... Try again: ')
print(f'You got it right with {hunches} attempts! Congratulations!')
