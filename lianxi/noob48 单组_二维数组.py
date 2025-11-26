n,m=map(int,input().split())
b=[]
add=0
for i in range(n):
    c=list(map(int,input().split()))
    b.append(c)
for i in range(n):
    for j in range(m):
        add+=b[i][j]
print(add)
'''主要是对python中二维数组的一些记忆'''