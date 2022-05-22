# Develop a program that reads the first term and the reason for a PA (Arithmetic Progression). At the end, show the first 10 terms of this progression.

first = int(input('First term: '))
reason = int(input('Reason: '))
tenth = first + (10 - 1) * reason
for c in range(first, tenth + reason, reason):
  print(f'{c} ', end='→ ')
print('FINISHED')
