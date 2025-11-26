a=int(input())
b=[]
d=0
for i in range(a):
    c=list(map(int ,input().split()))
    b.append(c)
for i in range(a):
    for j in range(i):
        if b[i][j]!=0:
            d+=1
if d==0:
    print("YES")
else:
    print("NO")        
     

