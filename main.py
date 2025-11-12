basket = ['a', 'x', 'b', 'c', 'd', 'e']
basket.sort() # mutate the original list

print(basket)
print(sorted(basket)) # create a sorted list

new_basket = basket.copy()
new_basket.reverse()
print(new_basket)