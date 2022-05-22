# Develop a program that reads two integers and shows the sum of only those that are even. If the value entered is odd, disregard it

summ = 0
counter = 0
for c in range(1, 7):
  number = int(input(f'Digite o {c} valor: '))
  if number % 2 == 0:
    summ += number
    counter += 1
print(f'You entered {counter} EVEN numbers and the sum was {summ}.')
