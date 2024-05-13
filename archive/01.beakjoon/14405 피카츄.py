# https://www.acmicpc.net/problem/14405


S = input()

pikachu = ['pi', 'ka', 'chu']

for i in pikachu:
    if i in S:
        S = S.replace(i, '@')
        
#@@@@@@
a = 0
for i in S:
    if i == '@':
        pass
    else:
        a+=1
        
print('YES' if a==0 else 'NO')
