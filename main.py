# Sets
# unordered collection of unique objects

my_set = {1,2,3,4,5,5}
print(my_set)

my_list = [1,2,3,4,5,5]
print(set(my_list))

print(len(my_set))

new_set = my_set.copy()
my_set.clear()

print(my_set)
print(new_set)