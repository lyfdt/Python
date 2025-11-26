import math
a=int(input())
def is_prime_optimized(i):
        if i==1:
            return "No"
        elif i==2:
            return "Yes"
        elif i%2==0:
            return "No"
        else:
            for b in range(3,int(math.sqrt(int(i)))+1,2):
                if i%b==0:
                    return "No"
            return "Yes"                      
for i in range(a):
    b=int(input())
    c=is_prime_optimized(b)
    print(c)                    
                  