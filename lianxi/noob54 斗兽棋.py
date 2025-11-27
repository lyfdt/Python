def animal(a,b):
    if (a=='elephant' and b=='tiger') or (a=='tiger' and b=='cat') or(a=='cat' and b=='mouse') or (a=='mouse' and b=='elephant'):
        print('win')
    elif (b=='elephant' and a=='tiger') or (b=='tiger' and a=='cat') or(b=='cat' and a=='mouse') or (b=='mouse' and a=='elephant'):
        print('lose')
    else:
        print('tie')
a,b=map(str,input().split())
animal(a,b)
'''优化写法：
def animal(a,b):
    rules={'elephant':'tiger','tiger':'cat','cat':'mouse','mouse':'elephant'}
    if a==b:
        print('tie')
    elif rules[a]==b:
        print('win')
    else:
        print('lose')
        a,b=map(str,input().split())
        animal(a,b)
        使用键值对来近似表现大小关系，是解决字符串定义大小比较问题的常用方法
'''