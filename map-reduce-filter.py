from functools import reduce

def m_reduce():
    def add(x, y):
        return x + y
    res = reduce(add, [1, 2, 3])
    print(res)

def m_map():
    def m_g():
        num = 1
        while True:
            yield num + 1
    
    it = m_g() 

    res = map(lambda x: x*x , it) # 生成器可以被无限迭代 ，但由于map是惰性序列，程序只保留这个式子而不执行，程序正常结束
    # print(list(res)) # 访问了map，开始计算结果，因为生成器可以被无限迭代，因此无限循环 


def m_filter():
    def list_queue(): 
        num = 2
        while True:
            yield num 
            num += 1

    def not_divisible(n): 
        return lambda x : x % n != 0         
    
    def primes():
        it = list_queue() # 构造生成器
        while True:
            num = next(it)
            yield num
            it = filter(not_divisible(num) , it) 

    for n in primes() :
        if  n < 100:
            print(n)
        else: 
            break
        
m_filter()
            



