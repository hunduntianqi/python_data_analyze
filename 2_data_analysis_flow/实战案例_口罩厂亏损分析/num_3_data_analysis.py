"""
    数据分析:
        目的: 用适当的分析方法及工具, 对数据进行处理和分析, 提取有价值的信息, 总结出所研究对象的内在规律
        1. 基础知识:
            1.1 分组聚合操作:
                指按照某项规则对数据进行分组, 接着对分完组的数据执行总结性统计的操作（比如求和、求均值）, 该操作返回的是一个
                Series对象
                单层分组聚合:指针对某一个组进行操作
                    df.groupby(by='列名', as_index=False)['列索引'].mean()
                    单层分组操作 ==> DataFrame.groupby(by='列名', as_index=False):
                        by ==> 代表了想要对那一列数据进行分组操作
                        as_index ==> 选择是否包含自带行的索引, False为包含, True则为使用分组列名作为行索引(默认)
                    聚合操作 ==> ['列索引'].mean():
                        指定要对那列数据进行聚合操作
                多层分组聚合:指针对多个分组进行操作
                    df.groupby(by=['列名1', '列名2', ...], as_index=False)['列索引'].mean()
                    分组的顺序和列表中的参数是对应的(从左往右依次拆分)
                    s.unstack()方法:可以将一个多层分组聚合后的 Series 对象转变成 DataFrame 对象, 是针对多层分组聚合后
                                    的 Series 对象来使用的, 作用就是将其索引的最后一列转变成 DataFrame 对象的列索引，而
                                    剩下的索引则转变成 DataFrame 对象的行索引
            1.2 数据可视化:
                可以利用利用人对形状、颜色的感官敏感, 有效地传递信息, 帮助用户更直观地从数据中发现关系、规律、趋势
                折线图:
                    以折线的上升或下降来表示统计数量的增减变化的统计图, 一般用来展现数据随时间的变化趋势
                    pandas 库是根据一个更加底层的绘图库——matplotlib，封装而来
                    向matplotlib 库添加中文字体:
                        from matplotlib import pyplot as plt
                        plt.rcParams['font.family'] = ['中文字体']
                    绘制单条折线图:
                        Series.plot(kind, figsize, title):
                            kind: 设置图表类型, 参数值类型-字符串, 例: lind='line'
                            figsize: 设置图表的大小, 参数值类型-元组(宽, 高), 单位是英寸, 例: figsize=(7, 7)
                            title: 设置图表标题, 参数值类型-字符串, 例: title='股价变化趋势图'
                    绘制多条折线图:
                        DataFrame.plot(kind, figsize, title):
                            kind: 设置图表类型, 参数值类型-字符串, 例: lind='line'
                            figsize: 设置图表的大小, 参数值类型-元组(宽, 高), 单位是英寸, 例: figsize=(7, 7)
                            title: 设置图表标题, 参数值类型-字符串, 例: title='股价变化趋势图'
                        显示图像方法: 绘图代码后加代码: pyplot.show() >> 注意: 该代码会阻塞程序继续运行
        2. 案例实战-数据分析
            2.1 分组聚合-统计数据
                分组聚合查询获取每月的销售额总数, 每月的单价平均值, 各月订单量总数, 各月各省订单量总数
            2.2 折线分析-确定趋势
                2.2.1 根据分组聚合查询结果绘制折线图
                2.2.2 观察折线图:
                    整体的走势
                    走势的规律性
                    走势的波动
            2.3 原因剖析-聚焦问题:
                2.3.1 聚焦最值
                2.3.2 内外因分析
                2.3.3 佐证解释
            2.4 深入洞察-提出对策
"""

import pandas as pd
from matplotlib import pyplot as plt

# 读取清洗好的数据
mask_clean = pd.read_csv(filepath_or_buffer='./需求数据/mask_data_clear.csv', sep=',', encoding='gbk', engine='python')
# 打印
print(mask_clean)
# # 单层分组聚合查询
# print(mask_clean.groupby('月份')['销售额'].sum())
# # 多层分组聚合查询
# print(mask_clean.groupby(['省', '月份'])['销售额'].sum().unstack())
#
# print(type(mask_clean.groupby('省')['销售额'].sum()))
# print(mask_clean.groupby('省')['销售额'].sum().plot(kind='line', figsize=(7, 7)))

# 绘制折线图
# 向matplotlib中添加中文字体
plt.rcParams['font.family'] = ['KaiTi']

'''数据分析'''
'''分组聚合查询'''
# 分组聚合查询获取每月的销售额总数
month_total = mask_clean.groupby(by='月份', as_index=False)['销售额'].sum()
print(month_total)
# 分组聚合查询获取每月的单价平均值
price_average = mask_clean.groupby('月份')['单价'].mean()
print(price_average)
# 分组查询各月订单量总数
order_total_month = mask_clean.groupby('月份')['订单量'].sum()
# 分组聚合查询各月各省订单量总数, 并转化为DataFrame对象
order_total_site_month = mask_clean.groupby(by=['省', '月份'], as_index=False)['订单量'].sum().unstack()
print("=======================")
print(order_total_site_month)
order_total_month_site = mask_clean.groupby(['月份', '省'])['订单量'].sum().unstack()
print("=======================")
print(order_total_month_site)

'''数据可视化-绘制折线图'''
# 各月总销售额
month_total.plot(kind='line', figsize=(7, 7), title='各月总销售额趋势图')
plt.show()
# 各月单价平均值
price_average.plot(kind='line', figsize=(7, 7), title='各月单价平均值趋势图')
plt.show()
# 各月订单量总数
order_total_month.plot(kind='line', figsize=(7, 7), title='各月订单量趋势图')
plt.show()
# 各省各月订单量趋势图
# print(order_total_site_month.plot(kind='line', figsize=(7, 7), title='各省各月订单量趋势图'))
# plt.show()
# 各月各省订单量趋势图
order_total_month_site.plot(kind='line', figsize=(7, 7), title='各月各省订单量趋势图')
plt.show()
