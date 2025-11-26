a=input()
b=int(a[5:7:])
if((b>=3) and (b<=5)):
    print("spring")
elif((b>=6) and (b<=8)):
    print("summer")
elif((b>=9) and (b<=11)):
    print("autumn")
else:
    print("winter")