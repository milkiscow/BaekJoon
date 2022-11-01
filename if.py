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

#




