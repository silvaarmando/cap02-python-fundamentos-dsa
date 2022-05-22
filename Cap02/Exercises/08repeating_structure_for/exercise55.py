# Create a program that reads any sentence and says if it is a palindrome, disregarding spaces.

# Exemples in Portuguese: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

phrase = str(input('Type a phrase: ')).strip().upper()
words = phrase.split()
together = ''.join(words)
reverse = together[::-1]
# for letter in range(len(together) - 1, -1, -1):
#   reverse += together[letter]
print(f'The reverse of {together} is {reverse}')
if reverse == together:
  print('The typed phrase is a palindrome')
else:
  print('The typed phrase is not a palindrome')
