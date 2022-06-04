class A: __slots__ = ('a','b')
class B: __slots__ = ('a','c')

a = A()
b = B()

b.b = 'b'  # 'B' object has no attribute 'b'



