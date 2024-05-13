# 풀이
S = input()

a = [
    'a','b','c','d','e','f','g','h','i','j','k',
    'l','m','n','o','p','q','r','s','t','u','v',
    'w','x','y','z'
]

for i in a:
    if i in S:
        print(S.index(i))
    if i not in S:
        print(-1)
        
# 다른 풀이

a = input()
for i in range(97, 123):
    print(a.find(chr(i)))
