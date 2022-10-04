from collections import UserList

class MyClass(UserList):

    def __init__(self, arg=None):

        super().__init__()

        if arg is not None:
            self.data = arg
        else:
            self.data = [1,2,3,4]

    def __repr__(self):
        return self.data[0]

    def __getitem__(self, i):
        return self.__class__(self.data[i])

a = MyClass()
print(len(a))
print(len(a[0:3]))