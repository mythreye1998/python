from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    i = input().split()
    getattr(d,i[0])(*[i[1]] if len(i)>1 else [])
print(*[it for it in d])
    
    
    
    