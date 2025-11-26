import math
a,b=map(float,input().split())
c,d=map(float,input().split())
de=float(math.sqrt(math.pow(a-c,2)+math.pow(b-d,2)))
dm=float(abs(a-c)+abs(b-d))
x=float(abs(dm-de))
print(f"{x:.9f}")
'''用到了两个库函数sqrt和pow，abs()不是math库里面的'''