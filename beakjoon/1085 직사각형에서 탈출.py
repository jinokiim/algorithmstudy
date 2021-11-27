x, y, w, h = map(int, input().split())

def find_d(x, y, w, h):
    return min(h-y, w-x, y, x)

print(find_d(x,y,w,h))
