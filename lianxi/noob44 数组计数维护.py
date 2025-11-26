a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    d=list(map(int,input().split()))
    s,cnt=0,0
    for j in range(b):
        if(d[j]>=c):
            s+=d[j]
        elif(d[j]==0 and s>=1):
            s=s-1
            cnt=cnt+1
    print(f"{cnt:d} ")        



