quote = 'to be or not to be'

print(quote.upper()) # TO BE OR NOT TO BE
print(quote.capitalize()) # To be or not to be

print(quote.find('be')) # 3
print(quote.replace('be', 'me'))

print(quote) # still "to be or not to be" because strings are immutable

quote2 = quote.replace('be', 'me')
print(quote2) # "to me or not to me"