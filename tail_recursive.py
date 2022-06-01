def fact(num , res):
    if(num == 1):
        return res # 返回相乘结果 
    return fact(num - 1 , res * num) # 将相乘结果和下一轮要乘的数传给下一个函数

def run(num):
    return fact(num , 1) # 1作为初始结果

print(run(5))  # 120