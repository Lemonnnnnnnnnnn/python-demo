class Desc:
    def __init__(self, name):
        self.name = name
    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.name
class A:
    x = Desc('Tom')

a = A()
print(a.x)    # 打印了 'Retrieving'