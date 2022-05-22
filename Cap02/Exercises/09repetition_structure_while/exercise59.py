# Make a program that reads the gender of a person, but only accept the values ​​'M' or 'F'. If it is wrong, ask for the typing again until it has a correct value.

sex = str(input('Enter your gender: [M/F] ')).strip().upper()[0]
print(sex)
while sex not in 'MmFf':
  sex = str(input('Invalid data. Please enter your gender:')).strip().upper()[0]
print(f'Gender {sex} successfully recorded')
