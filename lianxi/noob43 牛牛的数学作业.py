a=int(input())
for i in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    print(max(arr)-min(arr),end=" ")
    c=sum(arr)/b
    d=sum((n-c)**2 for n in arr)/b
    print(f"{d:.3f}")
# 一些库函数的使用