"""
    查看数据的分布或者排序, 一般考虑使用柱状图来呈现

"""
import pandas as pd
from matplotlib import pyplot as plt

# 为matplotlib库添加中文字体
plt.rcParams['font.family'] = ['KaiTi']
basic_data = pd.read_csv(filepath_or_buffer='./需求数据/公众号用户访问数据-强关联规则.csv', sep=',', encoding='gbk', engine='python')
# 设置横纵坐标及柱子的宽度
width = 0.2
# 设置画布
plt.figure(figsize=(20, 7))
# 绘制柱状图
plt.bar(basic_data.index - width / 2, basic_data['支持度'], color='b', alpha=0.5, width=width)
plt.bar(basic_data.index + width / 2, basic_data['置信度'], color='r', alpha=0.5, width=width)
plt.bar(basic_data.index + width * 3 / 2, basic_data['提升度'], color='y', alpha=0.5, width=width)
# 设置图例
plt.legend(['支持度', '置信度', '提升度'])
# 设置横坐标刻度名称
plt.xticks(basic_data.index, basic_data['关联规则'], fontsize=8, rotation=0)
# 设置标题
plt.title('强关联规则分布图', fontsize=25)
# 设置坐标标题
plt.xlabel('关联规则', fontsize=20)
plt.ylabel('数值', fontsize=20)
# 设置数据标签
x = basic_data.index
y1 = basic_data['支持度']
for a, b in zip(x, y1):
    plt.text(a - width / 2, b, '%0.2f' % b, ha='center', va='bottom', fontsize=10)
y2 = basic_data['置信度']
for a, b in zip(x, y2):
    plt.text(a + width / 2, b, '%0.2f' % b, ha='center', va='bottom', fontsize=10)
y3 = basic_data['提升度']
for a, b in zip(x, y3):
    plt.text(a + width * 1.5, b, '%0.2f' % b, ha='center', va='bottom', fontsize=10)
plt.savefig('./需求数据/强关联规则分布图.png')
plt.show()
