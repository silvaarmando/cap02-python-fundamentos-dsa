name = str(input('Digite seu nome: '))
for_bin = bin(int.from_bytes(name.encode(), 'big'))
print(f'O nome {name} em binário é {for_bin[2:]}')