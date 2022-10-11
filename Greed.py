#11399                  lst1 정수로 변환 안하면 틀림.
N = int(input())
lst1 = input().split()
for i in range(N):
    lst1[i] = int(lst1[i])
lst1.sort()
lst2 = []
j = 0
for i in lst1:
    j += int(i)
    lst2.append(j)
print(sum(lst2))

#11047                  예제 넣었을때는 되는데 제출시 틀림.
N, M = input().split()
N, M = int(N), int(M)
n = 0
lst1 = []
for i in range(N):
    lst1.append(input())
for i in range(N):
    lst1[i] = int(lst1[i])
lst1.sort()
for i in range(N-1, -1, -1):
    m = M // lst1[i]
    n += m
    M -= m*lst1[i]
    print(i, end=' ')
    print(m)
print(n)

#1026
N = int(input())
A, B = list(map(int, input().split())), list(map(int, input().split()))
A.sort(reverse = True)
B.sort()
S = 0
for i in range(N):
    S += A[i]*B[i]
print(S)

#5585
p = 1000 - int(input())
c = [500, 100, 50, 10, 5, 1]
m = 0
for i in c:
    n = p // i
    p -= i * n
    m += n
print(m)

#













