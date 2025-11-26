'''法1
a=int(input())
b=0
for i in range(0,a+1):
    b+=i
    
print(b) 没有格式对齐,无缩进表示推出循环


法2
a = int(input())
print(sum(range(1, a + 1)))
'''
a=int(input())
Sum=int(a*((1+a)/2))
print(Sum)