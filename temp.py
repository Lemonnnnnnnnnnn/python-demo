class A:
    # __slots__ = ('__name')
    def __init__(self):
        self.__name = 'a'
    
    def get_name(self):
        print(self.__name)

a = A()
a.get_name()

