# Create a program that reads the *name*, age and gender of various people. For each person registered, the program must ask whether the user wants to continue or not. No end, show:

# A) How many people are over 18?

# B) How many men were registered.

# C) How many women are under 20 years old.

total18 = total_male = total_trans = total_woman20 = 0
while True:
  name = str(input('Name: '))
  age = int(input('Age: '))
  gender = ' '

  while gender not in 'MFT':
    gender = str(input('Gender: [ M -> Male / F -> Female / T -> Trans ] ')).strip().upper()[0]
  if age >= 18:
    total18 += 1
  if gender == 'M':
    total_male += 1
  if gender == 'T':
    total_trans += 1
  if gender == 'F' and age < 20:
    total_woman20 += 1


  response = ' '
  while response not in 'YN':
    response = str(input('Do you want to continue?  [Y / N] ')).strip().upper()[0]
  if response == 'N':
    break
print(f'Total of people over 18 years old: {total18}')
print(f'in all we have {total_male} men registered.')
print(f'we have {total_woman20} registered woman under 20 years old.')