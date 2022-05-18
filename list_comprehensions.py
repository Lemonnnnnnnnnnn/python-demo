
list = [x * x for x in range(1, 4)]  # [for前面的内容会被视为表达式]
print(list)  # [1, 4, 9]

list = [x * x for x in range(1, 4) if x % 2 == 0]  # 后面的被视为条件
print(list)  # [4]

list = [m + n for m in 'AB' for n in "DE"]  # 全排列
print(list)  # ['AD', 'AE', 'BD', 'BE']


obj = {'foo': 1, 'bar': 2}
# [('foo', 1), ('bar', 2)] 生成c++ pair结构数组
print([value for value in obj.items()])

str = ['Hello', 'World']
print([s.lower() for s in str]) # 快速处理每一个item ['hello', 'world']

