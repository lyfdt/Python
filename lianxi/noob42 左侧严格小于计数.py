a=int(input())
b = list(map(int, input().split()))
for i in range(a):
    count = 0
    for j in range(i): 
        if b[j] < b[i]:
            count += 1
    print(count, end=' ')