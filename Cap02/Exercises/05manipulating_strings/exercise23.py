"""n = str(n)
print(f'Analisando o número {n}, ele tem...')
print(f'Unidade: {n[0]}')
print(f'Dezena: {n[1]}')
print(f'Centena: {n[2]}')
print(f'Milhar: {n[3]}')"""
n = int(input('Type a number: '))
unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10
print(f'Analyzing the number {n}')
print(f'   Unity: {unidade}')
print(f'     Ten: {dezena}')
print(f' Hundred: {centena}')
print(f'Thousand: {milhar}')