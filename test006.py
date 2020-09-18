#/python3

import pygal

from Matp.test004 import De

# 创建两个D6骰子
de_1 = De()
de_2 = De()

# 掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = de_1.roll() + de_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = de_1.num_sides + de_2.num_sides

