total = greader_thousand = counter = smaller = 0
cheap = ''
while True:
  product = "What's the product name? "
  price = "What's the price of the product? "
  total += price
  counter +=  1

  if price > 1000:
    greader_thousand += 1
  if counter == 1 or price < smaller:
    smaller = price
    cheap = product

  answer = ' '
  while answer not in 'SN':
    answer = str(input('Do u wish to continue? [S/N] ')).strip().upper()
  if answer == 'N':
    break

print('{:-^40'.format('END OF SESSION'))
print(f'The total purchase price was R$ {total} and {counter} products were purchased.')
print(f'the total of products costing more than R$ 1000 were {greader_thousand}')
print(f'The cheapest product purchased was {cheap} and it cost R$ {smaller}.')