a = 3
b = 4
saolei_1 = [[0 for _ in range(b)] for _ in range(a)]

# 美化输出
for row in saolei_1:
    print(' '.join(map(str, row)))

print(saolei_1)
# 输出：[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]