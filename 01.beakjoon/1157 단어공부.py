getword = input().upper()
wordlist = list(set(getword))
counter=[]

for word in wordlist:
    counter.append(getword.count(word))

if counter.count(max(counter))>1:
    print('?')

else:
    print(wordlist[counter.index(max(counter))])
