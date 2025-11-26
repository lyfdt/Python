num=list(map(int,input().split()))
num=num[:-1]
num.reverse()
print(' '.join(map(str,num)))
'''
join() 是字符串的方法，不是列表的方法

参数必须是字符串的序列（列表、元组等）

效率比用 + 拼接字符串高很多

所以在你的题目中，' '.join(map(str, nums)) 的意思就是：

map(str, nums)：把数字列表转换成字符串列表

' '.join(...)：用空格把这些字符串连接起来
'''