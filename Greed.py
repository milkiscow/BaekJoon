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

#11047                  예제 넣었을 때는 되는데 제출시 틀림. >>> 고쳤음(10.24)
N, M = map(int, input().split())
n = 0
lst1 = []
for i in range(N):
    lst1.append(int(input()))
lst1.sort(reverse = True)
for i in range(N):
    m = M // lst1[i]
    n += m
    M -= m*lst1[i]
print(n)

#1026                   B 변경 안하고 하는법 모르겠음.
N = int(input())
A, B = list(map(int, input().split())), list(map(int, input().split()))
A.sort(reverse = True)
B.sort()
S = 0
for i in range(N):
    S += A[i]*B[i]
print(S)

#5585                   쉬움.
p = 1000 - int(input())
c = [500, 100, 50, 10, 5, 1]
m = 0
for i in c:
    n = p // i
    p -= i * n
    m += n
print(m)

#10162                  60점 받음.
T = int(input())
m = [600, 60, 10]
m_ = []
for i in m:
    n = T // i
    m_.append(n)
    T -= n * i
if T != 0:
    print(-1)
else:
    print(m_[0], m_[1], m_[2])

#1439                   str의 i, i+1번째를 비교해야한다는 힌트 받음.
S = input()
cnt = 0
for i in range(1, len(S)):
    if S[i-1] != S[i]:
        cnt += 1
if cnt%2 == 0:
    print(int(cnt/2))
else:
    print(int(cnt/2) + 1)

#2864                   쉬움.
n = input()
m1 = map(int, n.replace('6', '5').split())
m2 = map(int, n.replace('5', '6').split())
print(sum(m1), sum(m2))

#2720                   쉬움.
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
for i in lst:
    q = i//25
    i -= q*25
    d = i // 10
    i -= d*10
    n = i//5
    i -= n*5
    p = i//1
    i -= p*1
    print(q, d, n, p)

#2847                   쉬움.
n = int(input())
lst = []
cnt = 0
for i in range(n):
    lst.append(int(input()))
for i in range(n-1, 0, -1):
    while lst[i] <= lst[i-1]:
        lst[i-1] -= 1
        cnt += 1
print(cnt)

#11508                  쉬움. 근데 실행시간 오래걸림
N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
for i in range(2, len(lst), 3):
    lst[i] = 0
print(sum(lst))

#14720                  실패, 이유 모르겠음. >>> 고쳤음(10.24)
N = int(input())
lst = list(map(int, input().split()))
m = lst.index(0)
n = 0
cnt = 1
for i in range(m, N):
    if n + 1 == lst[i]:
        n += 1
        cnt += 1
    elif n == 2 and lst[i] == 0:
        n = 0
        cnt += 1
print(cnt) 

#14469                  쉬움.
N = int(input())
cows = []
T = 0
arrive = []
for i in range(N):
    cows.append(input().split())
    cows[i][0] = int(cows[i][0])
    cows[i][1] = int(cows[i][1])
# for i in range(N):
#     arrive.append(cows[i][0])
cows.sort()
for i in range(N):
    if T < cows[i][0]:
        T += cows[i][0] - T
    T += cows[i][1]
print(T)

#20044                  쉬움.
n = int(input())
k = 2*n - 1
lst = list(map(int, input().split()))
lst.sort()
m = []
for i in range(n):
    m.append(lst[i]+lst[k-i])
print(min(m))

#16435                  쉬움. 코드 줄이는법 참고함.
m = lambda: map(int, input().split())
N, L = m()
for i in sorted(m()):
    if L >= i:
        L += 1
print(L)

#






