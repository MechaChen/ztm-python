# Immutability

selfish_1 = '01234567'
selfish_1 = 100

print(selfish_1)


# String is immutable, so we can't change the value of the string
selfish_2 = '01234567'
selfish_2[0] = '8'

print(selfish_2) # TypeError: 'str' object does not support item assignment


# But we can change the value of the variable
selfish_3 = '01234567'
selfish_3 += '8'

print(selfish_3)