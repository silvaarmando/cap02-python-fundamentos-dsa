# Make a program that reads any number and shows its factorial

# Example:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# from math import factorial

# value = int(input('Enter a number to calculate your factorial: '))
# fact = factorial(value)
# print(f'The factorial of {value} is {fact}')

value = int(input('Enter a number to calculate your factorial: '))
calc = value
fact = 1
print(f'Calculando {value}! = ', end='')
while calc > 0:
  print(f'{calc}', end='')
  print(' x ' if calc > 1 else ' = ', end='')
  fact *= calc
  calc -= 1
print(f'{fact}')
