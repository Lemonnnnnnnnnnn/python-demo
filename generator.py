g = (x * x for x in range(10))  # 将列表生成器的[]转化成()就是生成器


def fib(num):  # 带 yield 的就是生成器
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        n += 1
        a, b = b, a+b
    return 'done'


for n in fib(6):  # 通过for in 获取yield的值
    print(n)

g = fib(6)


while(True):
    try:
        print(next(g))  # 通过next(生成器)获取yield的值
    except StopIteration as e:
        print("return :" , e.value) # 最后一次调用会报错，用错误捕获拿到return值
        break
