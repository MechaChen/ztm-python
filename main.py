# Short Circuiting

is_friend = True
is_user = True

# 'or' is more performant than 'and', since it would only check 1st if true, then stop

if is_friend or is_user:
  print('best friend forever')