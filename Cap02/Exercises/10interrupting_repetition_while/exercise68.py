summ = count = 0

while True:
  number = int(input('Digite um valor (999 para parar): '))
  if number == 999:
    break
  count += 1
  summ += number
print(f'A soma dos {count} valores foi {summ}.')
