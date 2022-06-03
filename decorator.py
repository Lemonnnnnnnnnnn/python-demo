def log(user , operate):
    def decorator(func):
        print(user, operate , func.__name__) # 打印函数名
        return lambda *args , **kwargs : func(*args , **kwargs)
    return decorator

@log('root' , 'call')
def hello(name):
    print('hello' ,name)

hello('liming') # root call hello hello liming


