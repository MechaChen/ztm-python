def highest_even(li):
  # do not hint me
  highest_even = 0
  for item in li:
    if item % 2 == 0:
      highest_even = item if item > highest_even else highest_even
    else:
      continue
  return highest_even

print(highest_even([10,2,3,4,8,11]))