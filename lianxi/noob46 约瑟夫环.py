a,b,c=map(int,input().split())
L=[i for i in range(a)]
for i in range(1,a):
    b=(b+c-1)%a
    a-=1
    L.remove(L[b])
print(L[0])