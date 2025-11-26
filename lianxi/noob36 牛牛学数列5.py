n=int(input())
def fibonaci(n):
    
    if(n<=2):
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
a=print(fibonaci(n))    

# 推荐写法
''' n = int(input())
def fibonacci(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b
print(fibonacci(n))'''