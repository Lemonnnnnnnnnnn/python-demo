
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
r2 = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))
print(list(r2))


print((lambda x: x*x)(2))  # 4

def f2(x):
    return lambda n : x * n

print( f2(2)(3) ) # 6
