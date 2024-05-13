n = set(range(1, 10001))
notnum = set()

for i in n:
    for j in str(i):
        i += int(j)
    
    notnum.add(i)
selfnum = n - notnum

for i in sorted(selfnum):
    print(i)
