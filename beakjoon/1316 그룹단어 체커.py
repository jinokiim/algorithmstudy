N = int(input())
checker = N

for i in range(N):
    word = (input())
    for i in range(len(word)-1): 
        if word.find(word[i])>word.find(word[i+1]):  
            checker -=1
            break
print(checker)
