print('             First & Last              ')
print('_______________________________________')
print('Very pleased to meet you')
n = str(input('Type your full name: '))
name = n.split()
first = name[0]
print(f'Your first name is {first}')
last = name[len(name)-1]
print(f'Your last name is {last}')
print('_______________________________________')
