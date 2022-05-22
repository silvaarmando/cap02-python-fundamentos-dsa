primeiro_num = int(input('Primeiro número: '))
segundo_num = int(input('Segundo número: '))
if primeiro_num > segundo_num:
    print(f'O primeiro número {primeiro_num} é maior que o segundo {segundo_num}.')
elif segundo_num > primeiro_num:
    print(f'O segundo número {segundo_num} é maior que o primeiro {primeiro_num}.')
elif primeiro_num > segundo_num:
    print(f'O primeiro número {primeiro_num} e o segundo {segundo_num} são iguais.')
else: 
    print('Os números são IGUAIS.')