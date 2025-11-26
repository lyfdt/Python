a=int(input())
def an(n):
    if n==1:
        return 0
    elif n==2 or n==3:
        return 1
    else:
        return an(n-3)+2*(an(n-2))+an(n-1)
print(an(a))        
