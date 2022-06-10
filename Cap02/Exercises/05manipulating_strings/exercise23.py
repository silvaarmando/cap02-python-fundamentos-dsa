"""n = str(n)
print(f'Analisando o número {n}, ele tem...')
print(f'Unidade: {n[0]}')
print(f'Dezena: {n[1]}')
print(f'Centena: {n[2]}')
print(f'Milhar: {n[3]}')"""

n_interger = int(input('Type a integer: '))
unity = n_interger // 1 % 10
ten = n_interger // 10 % 10
hundred = n_interger // 100 % 10
thousand = n_interger // 1000 % 10
print(f'Analyzing the number {n_interger}')
print(f'   Unity: {unity}')
print(f'     Ten: {ten}')
print(f' Hundred: {hundred}')
print(f'Thousand: {thousand}')