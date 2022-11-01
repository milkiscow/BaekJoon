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























