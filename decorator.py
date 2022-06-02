def log(func):
    print('call' , func.__name__) # 打印函数名
    return lambda *args , **kwargs : func(*args , **kwargs)

@log
def hello(name):
    print('hello' ,name)

hello('liming') # call hello , hello liming
