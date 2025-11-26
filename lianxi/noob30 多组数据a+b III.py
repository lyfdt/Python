
while True:
    b,c=map(int,input().split())
    if(b==0 and c==0):
         break
    print(b+c)     
    'python中while循环的条件不用打（），构造死循环最好用while循环，for in 不太好构建'