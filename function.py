def add_end(l=[]):
    l.append('end')
    print(l)


add_end()  # ['end']
add_end()  # ['end' , 'end']

def add_end2(l=None):
    if(l == None):
        l = []
    l.append('end')
    print(l)

add_end2()  # ['end']
add_end2()  # ['end']

def func(*rest , **kw):
    print(rest) # (1, 2, 3, 4, 5, 6)
    print(kw) # {'city': 'beijing', 'age': 18}

a = [1, 2, 3]
b = [4, 5, 6]
c = {'city' : 'beijing' , 'age' : 18}

func(*a, *b , **c)

