#1330
A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
# print('>' if a > b else ('<' if a < b else '=='))         숏코딩 참고

#9498
N = int(input())
if N > 89:
    print('A')
elif N > 79:
    print('B')
elif N > 69:
    print('C')
elif N > 59:
    print('D')
else:
    print('F')
    
#2753
Y = int(input())
if Y % 400 == 0 or (Y%4==0 and Y%100!=0):
    print(1)
else:
    print(0)

#14681
x = int(input())
y = int(input())
if x > 0:
    print(1 if y > 0 else 4)
else:
    print(2 if y > 0 else 3)

#2884
H, M = map(int, input().split())
M -= 45
if M < 0:
    M += 60
    H -= 1
if H < 0:
    H += 24
print(H, M)

#2525
A, B = map(int, input().split())
C = int(input())
A += C // 60
B += C % 60
if B >= 60:
    B -= 60
    A += 1
if A >= 24:
    A -= 24
print(A, B)
#n=60*a+b+int(input())          숏코딩 참고.
#print(n//60%24,n%60)

#2480
lst = input().split()
m = []
for i in range(3):
    if lst[i] == lst[(i+1)%3]:
        m.append(int(lst[i]))
if len(m) == 3:
    print(10000+m[0]*1000)
elif len(m) == 1:
    print(1000+m[0]*100)
else:
    print(100*int(max(lst)))


