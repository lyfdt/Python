a=int(input())
b=0
c=0
for i in range(a+1):
    if(i==1):
        c=c+i
    elif(i%2==0):
        c=c-i
    else:
        c=c+i
    b=c
print(b)        
        # i是娶不到a+1的只能取到a
            
            
    