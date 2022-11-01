#2739
N = int(input())
for i in range(1, 10):
    print('{} * {} = {}' .format(N, i, N*i))

#10950
T = int(input())
for i in range(T):
    a,b = map(int, input().split())
    print(a+b)

#8393
n = int(input())
print(int(n*(n+1) / 2))

#25304
X = int(input())
N = int(input())
M = []
for i in range(N):
    a,b = map(int,input().split())
    M.append(a*b)
x = sum(M)
if X == x:
    print('Yes')
else:
    print('No')

#15552
import sys
T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

#11021
import sys
T = int(input())
for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #{}: {}' .format(i, a+b))
    
#11022
import sys
T = int(input())
for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #{}: {} + {} = {}' .format(i, a, b, a+b))

#2438
N = int(input())
for i in range(1, N+1):
    print('*' * i)

#2439
N = int(input())
for i in range(1, N+1):
    print(('*'*i).rjust(N))






