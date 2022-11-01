#2557
print('Hello World!')

#10718
print('강한친구 대한육군\n'*2)

#1000
a,b=map(int,input().split())

print(a+b)
# print(eval('+'.join(input())))            숏코딩참고

#1001
a,b=map(int,input().split())
print(a-b)

#10998
a,b=map(int,input().split())
print(a*b)

#1008
a,b=map(int,input().split())
print(a/b)

#10869
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

#10926
n = input()
print(n+'??!')

#18108
y = int(input())
print(y-543)

#3003
lst = list(map(int, input().split()))
ch = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(ch[i] - lst[i])

#10430                  코드 거의 똑같은데 시간 10ms 차이 나는 이유 모르겠음.
a,b,c=map(int,input().split())
print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)

#2588
a = int(input())
b = input()
re="".join(reversed(b))
lst = []
for i in range(len(re)):
    lst.append(a*int(re[i]))
    print(lst[i])
for i in range(len(lst)):
    lst[i] = lst[i] * (10**i)
print(sum(lst))

#10171
print('''\    /\\
 )  ( ')
(  /  )
 \(__)|''')

#10172
print('''|\_/|
|q p|   /}
( 0 )"""\\
|"^"`    |
||_/=\\\\__|''')

#25083
print('''         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |''')


