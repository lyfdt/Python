a,b=map(int,input().split())
put= [list(input().strip()) for _ in range(a)]
output = [['0' for _ in range(b)] for _ in range(a)]
c=[-1,-1,-1,0,0,1,1,1]
d=[1,0,-1,-1,1,1,0,-1]#这两个坐标很关键，节约了时间
for i in range(a):
    for j in range(b):
        if (put[i][j]=='*'):
            output[i][j]='*'
        else:
            count=0
            for k in range(8):
                dx,dy=i+c[k],j+d[k]
                if 0<=dx<a and 0<=dy<b and put[dx][dy]=='*':
                    count+=1
            output[i][j]=str(count)
for row in output:
    print("".join(row))        
            


