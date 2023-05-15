"""
    数据展现:
        数据展现工具:
            1. Tableau: 制作交互式数据可视化看板
                适合人群: 偏商业分析, 倾向于分析师
                可视化特点: 更具标准化
                收费: 70美元/用户/月
            2. Power BI: 创建个性化的数据看板, 与Excel完美兼容
                适合人群: 所有类型用户
                可视化特点: 更具定制化
                收费: Desktop版本免费, 自定义和共享仪表板需要9.99美元/月
            3. Python: 调用第三方可视化库作图, 图标种类非常多
                适合人群: 有一定编程基础
                可视化特点: 定制化非常强
                收费: 免费
                常用第三方可视化库: pandas, matplotlib和seaborn
        使用matplotlib库绘图:
            matplotlib库: 较于 pandas 绘图以及 seaborn 绘图工具更为底层, 绘图函数与参数相对更多, 可以与与numpy库, pandas库
                          并驾齐驱
            库的导入: from matplotlib import pyplot as plt
            绘图基础知识:
                1. 画布的生成与保存:
                    生成画布: plt.figure(figsize=(宽, 高))
                    保存画布: plt.savefig(path)
                2. 绘制图表:
                    2.1 设置x/y坐标值:
                        x坐标: 指坐标点的横坐标, 为可迭代对象, 可以理解为有序的元素序列, 例: x = (x1, x2, x3, ……, xn)
                        y坐标: 指坐标点的纵坐标, 为可迭代对象, 可以理解为有序的元素序列, 例: y = (y1, y2, y3, ……, yn)
                    2.2 绘制折线图和柱状图:
                        折线图函数: plt.plot(x, y, linewidth=3, color='red', marker='o', markersize=10, markerfacecolor='w')
                            x: 表示x坐标值
                            y: 表示y坐标值
                            该函数会自动将两个对象中的元素按照顺序匹配成坐标点, 并绘制成折线图
                            linewidth: 线条粗细
                            color: 线条颜色
                            marker: 数据标记形状
                            markersize: 数据标记大小
                            markerfacecolor: 数据标记填充颜色
                        柱状图函数: plt.bar(x, height)
                            x: 表示x坐标值
                            height: 表示柱子的高, 对应y坐标值
                    2.3 设置图表标题、坐标轴、图例以及数据标签:
                        2.3.1 设置图表标题-plt.title(label, fontsize=None)函数:
                            label: 标题名, 一般为字符串格式
                            fontsize: 标题的字体大小, 常见为数值类型
                            如果你想设置更丰富的字体样式，可以用 fontdict 参数代替 fontsize
                            fontdict: 是一个包含许多参数的字典
                                例: fontdict={'family': 'Source Han Sans CN', 'color': 'blue', 'weight': 'bold', 'size': 16}
                                fontdict不仅可以设置图表标题的字体样式, 还可以应用在坐标轴、图例、数据标签等图表元素
                        2.3.2 设置坐标轴
                            坐标轴刻度设置:
                                x轴: plt.xticks(fontsize, rotation)
                                    rotation: 旋转刻度字体方向
                                y轴: plt.yticks(fontsize)
                            坐标轴标题设置:
                                x轴: plt.xlabel(xlabel, fontsize=None)
                                y轴: plt.ylabel(ylabel, fontsize=None)
                        2.3.3 设置图例:
                            plt.legend(labels)函数:
                                参数labels: 表示图例名称, 对应图中的多个条件,通常传入可迭代对象, 比如列表, Series对象等
                        2.3.4 设置数据标签:
                            数据标签-坐标点上方显示的标签, 用于呈现每个坐标点的数据信息
                            plt.text(x, y, s, ha, va, fontsize)函数:
                                x / y: 表示数据标签的位置, 常见为数值或字符串类型
                                s: 表示数据标签的文本内容, 常见为数值或字符串类型
                                ha: 表示水平对齐方式, 可选'left', 'right', 'center'等
                                va: 表示垂直对齐方式, 可选'center', 'top', 'bottom'
                                fontsize: 表示数据标签的字体大小, 常见为数值类型
                                该函数每次只能添加一个数据标签
                                使用zip()函数结合for循环为图表添加数据标签
                                zip()函数: 可以将两个可迭代对象对应索引的数据取出组合为一个元组
                    Series对象排序:
                        s.sort_values()方法:
                            对 Series 对象的数值型数据进行排序, 默认为升序排列(从小到大),
                            将 ascending 参数设置为 False 就可以让它降序排列(从大到小)
        案例实战-数据展现:
            1. 选择对应图表:
                折线图: 呈现数据变化的趋势
                柱状图: 让数值大小的比较更加明显
                饼图: 直观的显示各部分相对于整体的占比
            2. 明确数据展现的目标:
                2.1 各月销售总额分布图
                2.2 各月平均单价分布图
                2.3 各月总订单量趋势
                2.4 各月各省订单量分布

    报告撰写:
        目的: 将分析结果, 建议以及其他有价值的信息传递给读者
        报告形式:
            1. Word:
                优势: 易于排版, 可打印装订成册
                劣势: 缺乏交互性, 不适合演示汇报
            2. Excel:
                优势: 可含有动态图表, 结果可实时更新, 交互性更强
                劣势: 不适合演示汇报
            3. PowerPoint:
                优势: 可加入丰富的元素, 适合演示汇报, 增强演示效果
                劣势: 不适合大篇文字
        报告结构:
            一般采用总分总结构, 包括: 背景, 目的, 分析思路, 分析正文, 结论和建议, 附录等
            背景: 阐述进行数据分析的原因, 意义, 以及其他相关信息, 比如公司现阶段的经营情况
            目的: 这次分析要解决什么问题, 达到何种目的
            分析思路: 用到了什么分析方法, 得到的分析框架是什么
            分析正文: 报告的主体部分, 包含所有的数据事实和观点, 通过数据图表和文字呈现, 一般分为三个部分:
                a. 数据来源: 解释数据的来源, 并展示数据的基本情况
                b. 数据处理: 进行了哪些数据处理操作以及处理的结果是什么
                c. 数据分析: 以图文结合的方式展示分析过程和结果, 并能证明分析过程合理, 分析结果能够应用于实际的工作场景
            结论和建议: 以综述性文字展现数据分析结果, 并结合公司的具体业务或问题给出建议
            附录: 提供正文涉及到的, 但是未详细阐述的资料, 一般包括名词解释, 源数据, 分析代码等, 为整个报告提供分析说明
        案例实战-报告撰写:

"""
# 导入pandas库
import pandas as pd
# 导入matplotlib库
from matplotlib import pyplot as plt

# 为matplotlib库添加中文字体
plt.rcParams['font.family'] = ['KaiTi']
# 读取数据
mask_data_clean = pd.read_csv(filepath_or_buffer='./需求数据/mask_data_clear.csv', sep=',', encoding='gbk', engine='python')
print(mask_data_clean)
# 分组查询获取各月订单总量
order_number = mask_data_clean.groupby('月份')['订单量'].sum()
print(order_number)
# 分组查询各月各省订单量
order_number_df = mask_data_clean.groupby(['月份', '省'])['订单量'].sum().unstack()
print(order_number_df)
# 分组查询各月平均单价
price_month = mask_data_clean.groupby('月份')['单价'].mean()
print(price_month)
# 分组查询各月销售总额
sales_all = mask_data_clean.groupby('月份')['销售额'].sum()
print(sales_all)
''' 绘制各月订单总量趋势图 '''
# 设置x坐标值
x = order_number.index
# 设置y坐标值
y = order_number.values
print(x, y)
# 生成画布
plt.figure(figsize=(6, 6))
# 绘制折线图
plt.plot(x, y, linewidth=3, color='red', marker='o', markersize=10, markerfacecolor='w')
# 设置图表标题
plt.title('各月订单总量趋势图', fontsize=20)
# 设置坐标轴刻度字体大小
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# 设置x / y坐标轴标题
plt.xlabel('月份', fontsize=15)
plt.ylabel('各月订单总量(百万)', fontsize=15)
# 添加数据标记
for a, b in zip(x, y):
    plt.text(a, b, b, ha='left', va='bottom', fontsize=10)
plt.savefig('./需求数据/各月订单总量趋势图.png')

''' 绘制各月各省订单量趋势图 '''
# 设置x / y坐标值
x_df = order_number_df.index
y_df = order_number_df.values
print(x_df, y_df)
# 生成画布
plt.figure(figsize=(7, 7))
# 绘制折线图
plt.plot(x_df, y_df, linewidth=3, marker='o', markersize=5)
# 添加图例
plt.legend(['其他', '广东', '江苏', '河南', '湖北', '湖南'])
# 设置图表标题
plt.title('各月各省订单总量趋势图', fontsize=20)
# 设置坐标轴刻度字体大小
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# 设置x / y坐标轴标题
plt.xlabel('月份', fontsize=15)
plt.ylabel('各月各省订单总量(百万)', fontsize=15)
plt.savefig('./需求数据/各月各省订单总量趋势图.png')

''' 绘制各月平均单价分布图 '''
# 设置x / y坐标
x_price = price_month.index
y_price = price_month.values
# 设置画布
plt.figure(figsize=(7, 7))
# 绘制柱状图
plt.bar(x_price, y_price, color=['r', 'g', 'g', 'g', 'g', 'b'], alpha=0.5, width=0.5)
# 设置图表标题
plt.title('各月平均单价', fontsize=20)
# 设置坐标刻度字体大小
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# 设置坐标标题
plt.xlabel('月份', fontsize=15)
plt.ylabel('平均单价(元)', fontsize=15)
# 设置数据标记
for a, b in zip(x_price, y_price):
    # b = int(b)
    plt.text(a, b, '%0.2f' % b, ha='center', va='center', fontsize=15)
plt.savefig('./需求数据/23_各月平均单价分布图.png')

''' 绘制各月销售总额分布图 '''
# 设置x / y坐标值
x_sales = sales_all.index
y_sales = sales_all.values
# 设置画布
plt.figure(figsize=(7, 7))
# 绘制柱状图
plt.bar(x_sales, y_sales, color='yellow', width=0.5, alpha=0.5)
# 设置图表标题
plt.title('各月销售总额', fontsize=20)
# 设置坐标刻度字体大小
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# 设置坐标标题
plt.xlabel('月份', fontsize=15)
plt.ylabel('各月销售总额(亿元)', fontsize=15)
# 设置数据标记
for a, b in zip(x_sales, y_sales):
    # b = int(b)
    plt.text(a, b, '%0.0f' % b, ha='center', va='center', fontsize=15)
plt.savefig('./需求数据/各月销售总额分布图.png')
plt.show()
