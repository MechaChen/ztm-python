class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList([0, 1, 2, 3, 4])
print(len(super_list1))
super_list1.append(5)
print(super_list1[5])
print(issubclass(SuperList, list))
print(issubclass(list, object))
