class Student:
    def __init__(self , name , age) :
        self.__name = name
        self.__age = age

    def get_name(self):
        print(self.__name)

class Monitor(Student):
    def __init__(self , name , age) :
        super().__init__(name , age) # 调用父类的构造器
       

    # def __init__(self , name , age) :
    #     self.__name = name
    #     self.__age = age

bart = Monitor('bart' , 18 )

bart.get_name()