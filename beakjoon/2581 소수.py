def find_sosu(M, N):
    sosu_list = []

    for number in range(M, N+1):
        count = 0
        if number==1:
            continue
        for i in range(2, int(number**0.5)+1):
            if number%i==0:
                count+=1
                break
        
        if count == 0:
            sosu_list.append(number)
    if len(sosu_list)==0:
        return -1
    else:
        return '{}\n{}'.format(sum(sosu_list), min(sosu_list))

M = int(input())
N = int(input())
print(find_sosu(M, N))
