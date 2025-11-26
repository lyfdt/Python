import math
a,b=map(int,input().split())
tree=[1]*(a+1)
for i in range(b):
    c,d=map(int,input().split())
    for j in range(c,d+1):
        tree[j]=0
print(sum(tree))
'''抄别人的，思路无敌'''