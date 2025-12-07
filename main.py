# Exercise: Check for duplicates in the list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

set = set()
duplicates = []

for item in some_list:
  if item in set:
    duplicates.append(item)
  else:
    set.add(item)

print(duplicates)


duplicates_two = []

for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates_two:
      duplicates_two.append(value)

print(duplicates_two)