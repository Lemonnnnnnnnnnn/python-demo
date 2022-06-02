def count():
    fs = []

    for i in range(1,4):
        
        def keep(num):  
            def compute():
                return num * num
            return compute
        
        fs.append(keep(i))
    return fs

f1,f2,f3 = count()

print(f1())  # 1


