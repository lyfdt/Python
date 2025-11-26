a=int(input())
b=[]
for i in range(a):
    c=[1]*(i+1)
    for j in range(1,i):
        c[j]=b[i-1][j]+b[i-1][j-1]
        b.append(c)
for i in range(a):
    for j in range(1,i):
        print(b[i][j])
    print()