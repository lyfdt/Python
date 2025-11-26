n, x = map(int, input().split())
num = 0
for i in range(1, n + 1):
    num+= str(i).count(str(x))
print(num)
'''  str(i) - 将整数 i 转换为字符串

例如：i = 15 → "15"

str(x) - 将目标数字 x 转换为字符串

例如：x = 1 → "1"

str(i).count(str(x)) - 在字符串 i 中统计字符串 x 出现的次数

例如："15".count("1") → 1（出现1次）

例如："11".count("1") → 2（出现2次）

count += ... - 将统计结果累加到总计数中 count计数函数的使用'''