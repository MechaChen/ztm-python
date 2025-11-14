# Conditional Logic

is_old = False
is_licenced = True

if is_old:
  print('you are old enough to drive!')
elif is_licenced:
  print('you can drive now!')
else:
  print('you are not of age!')

if is_old and is_licenced:
  print('you are old enough to drive, and you have a licence!')
else:
  print('you are not of age!')

print('okok')