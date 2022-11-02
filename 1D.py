#10807
N = int(input())
lst = list(map(int, input().split()))
M = int(input())
cnt = 0
for i in range(len(lst)):
    if lst[i] == M:
        cnt += 1
print(cnt)

#10871  
N, X = map(int, input().split())
lst = [i for i in input().split() if int(i) < X]
print(' '.join(lst))

#10818
N = int(input())
lst = list(map(int, input().split()))
print(min(lst), max(lst))

#2562
lst = [0]
for i in range(9):
    lst.append(int(input()))
print(max(lst), lst.index(max(lst)))

#5597
lst = list(range(1,31))
for i in range(28):
    lst.remove(int(input()))
print(lst[0])
print(lst[1])

#3052                   숏코딩 참고.
b = [int(input())%42 for i in range(10)]
print(len(set(b)))

#1546
N = int(input())
lst = list(map(int, input().split()))
M = max(lst)
for i in range(N):
    lst[i] = lst[i]/M*100
print(sum(lst)/N)














