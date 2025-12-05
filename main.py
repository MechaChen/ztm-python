my_list = [1,2,3]
for item in my_list:
  continue
  print(item)

i = 0
while i < len(my_list):
  i += 1
  continue
  print(my_list[i])

for item in my_list:
  # if nothing here, it will throw error
  # therefore, we can use `pass` to do nothing without throwing error
  pass