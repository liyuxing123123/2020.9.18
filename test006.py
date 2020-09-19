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
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('de_visual.svg')


