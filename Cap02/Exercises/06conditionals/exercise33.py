from datetime import date

year = int(input('Enter year to search (0 for current year): '))
if year == 0: 
  year - date.today().year
if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
  print(f'The year {year} is not leap.')
else:
  print(f'The year {year} is leap.')