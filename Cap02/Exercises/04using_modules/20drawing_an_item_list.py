from random import shuffle

first = str(input('First student: '))
second = str(input('Second student: '))
third = str(input('Third student: '))
fourth = str(input('Fourt student: '))
students = [first, second, third, fourth]
shuffle(students)
print(students)