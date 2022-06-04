class Student:
    def __init__(self):
        self._score = 60

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self , value):
        if not isinstance(value, int):
            print('score must be an integer!')
            return 
        if value < 0 or value > 100:
            print('score must between 0 ~ 100!')
            return
        self._score = value
    
xiaoming = Student()
xiaoming.score = 90
print(xiaoming.score) 