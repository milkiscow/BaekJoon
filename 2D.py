#2738
N, M = map(int, input().split())
mat1 = [list(map(int, input().split())) for i in range(N)]
mat2 = [list(map(int, input().split())) for i in range(N)]
mat3 = []
for i in range(N):
    lst = []
    for j in range(M):
        lst.append(mat1[i][j]+mat2[i][j])
    mat3.append(lst)
    print(' '.join(map(str, mat3[i])))
    
#2566
l = []
m = []
for i in range(9):
    lst = list(map(int, input().split()))
    l.append(lst)
    m.append(max(l[i]))
mm = max(m)
i1 = m.index(mm)
for i in range(9):
    if l[i1][i] == mm:
        i2 = int(i)
print(mm)
print(i1+1, i2+1)

#2563



















