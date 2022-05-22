# Develop a program that reads the name, age and sex of 4 people. At the end of the program, show:

# - The average age of the group.
# - What is the name of the older man.
# - How many women are under the age of 20.

sumage = 0
averageage = 0
adulthood = 0
oldname = ''
totwomen20 = 0

for p in range(1, 5):
  print(f'----- {p}st PERSON -----')
  name = str(input('Name: ')).strip()
  age = int(input('Age: '))
  sex = str(input('Gender [M/F]: ')).strip()
  print('\n')
  sumage += age
  if p == 1 and sex in 'Ff':
    adulthood = age
    oldname = name
  if sex in 'Ff' and age > adulthood:
    adulthood = age
    oldname = name
  if sex in 'Ff' and age < 20:
    totwomen20 += 1
averageage = sumage / 4
print(f'The average age of the group is {averageage} years.')
print(f'The older woman has {adulthood} age and is called {oldname}.')
print(f'Altogether there are {totwomen20} women under the age of 20.')