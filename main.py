a = 1

def parent():
  a = 10
  def confusion():
    return a
  return confusion()

print(parent())
print(a)

b = 2

def confusion_b():
  b = 20
  return b

print(confusion_b())
print(b)

# 1 - start with local scope
# 2 - then parent local scope
# 3 - then global scope
# 4 - then built-in python functions