class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 100


class D(B, C):
    pass


print(D.num)
print(D.__mro__)
