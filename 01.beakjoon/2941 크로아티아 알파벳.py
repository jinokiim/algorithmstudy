word = input()
calpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in calpha:
    word = word.replace(i, '*')

print(len(word))
