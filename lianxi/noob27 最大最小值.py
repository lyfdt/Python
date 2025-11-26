'''法1自己写的
a,b,c=map(int,input().split())
if(a>b>c):
        print(f"The maximum number is : {a:d}")
        print(f"The minimum number is : {c:d}")
elif(a>c>b):
    print(f"The maximum number is : {a:d}")
    print(f"The minimum number is : {b:d}")
elif(b>c>a):
    print(f"The maximum number is : {b:d}")
    print(f"The minimum number is : {a:d}")
elif(b>a>c):
    print(f"The maximum number is : {b:d}")
    print(f"The minimum number is : {c:d}")
elif(c>b>a):
    print(f"The maximum number is : {c:d}")
    print(f"The minimum number is : {a:d}")
elif(c>a>b):
    print(f"The maximum number is : {c:d}")
    print(f"The minimum number is : {b:d}")
else:
    print(f"The maximum number is : {c:d}")
    print(f"The minimum number is : {b:d}")'''
'用函数写法是借鉴ai的'
a, b, c = map(int, input().split())
max_num = max(a, b, c)
min_num = min(a, b, c)
print(f"The maximum number is : {max_num:d}")
print(f"The minimum number is : {min_num:d}")







    

