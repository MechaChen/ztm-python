basket = [1,2,3,4,5]

# adding
new_list = basket.append(100)
print(basket)
print(new_list) # None

basket.insert(4, 200)
print(basket)

basket.extend([101, 102])
print(basket)

# removing

## pop(): remove last, or by index
basket.pop()
print(basket)

popped = basket.pop(0)
print(popped)
print(basket)

## remove(): remove by value
basket.remove(200)
print(basket)

## clear(): remove all items
basket.clear()
print(basket)