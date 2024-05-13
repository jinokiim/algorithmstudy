# 첫버째 풀이

n =list(input())

time = 0
for i in n:
    if i=='A' or i=='B' or i=='C':
        time+=3
    if i=='D' or i=='E' or i=='F':
        time+=4
    if i=='G' or i=='H' or i=='I':
        time+=5
    if i=='J' or i=='K' or i=='L':
        time+=6
    if i=='M' or i=='N' or i=='O':
        time+=7
    if i=='P' or i=='Q' or i=='R' or i=='S':
        time+=8
    if i=='T' or i=='V' or i=='U':
        time+=9
    if i=='W' or i=='X' or i=='Y' or i=='Z':
        time+=10

print(time)

# 두번째 풀이

n = input()
dial = [3]*3+[4]*3+[5]*3+[6]*3+[7]*3+[8]*4+[9]*3+[10]*4
time=0
for i in n:
    time+=dial[ord(i)-65]
print(time)
