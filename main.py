# Value Equality: Check if two objects have the same value after conversion
print(True == 1)
print('1' == 1)
print([] == 1)
print(10 == 10.00)
print([] == []) # for Python, == for array and object will be deepEqual

# Identity Equality: Check if two objects are the same object in memory
print(True is 1)
print('1' is 1)
print([] is 1)
print(10 is 10.00)
print([] is [])

a = [1,2,3]
b = [1,2,3]
print(a is b)