class Foo: #在python3中Foo是新式类,它实现了三种方法,这个类就被称作一个描述符
    def __get__(self, instance, owner):
        print('__get__(),被执行了')
    def __set__(self, instance, value):
        print('__set__(),被执行了')
    def __delete__(self, instance):
        print('__delete__(),被执行了')
        
foo = Foo()
foo