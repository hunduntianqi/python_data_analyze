"""
    本次案例分析的是顾客在 '一次购买行为' 中放入 '购物篮' 的 '不同商品之间的关联', 因此适合 Apriori 算法计算的数据形式为:
        按照 'id' 进行分组聚合的 '文具' 数据
    数据处理:
        思路: 文具列数据由字符串转换成列表
            1. 先将"字符串"格式的文具列数据转换为"包含单个字符串的列表"格式
            2. 使用 df.groupby().sum()将同一 id 的 "包含单个字符串列表"数据聚合为"包含多个字符串列表"格式的数据
    数据分析:
        执行 Apriori 算法需要设置的参数包括数据集、最小支持度、最小置信度以及最小提升度
            1. 通过设置最小支持度筛选频繁项集, 即用户更有可能购买的商品
            2. 通过设置最小置信度筛选强关联规则, 即用户在购买某商品时, 更倾向于或更不倾向于购买的另外一个商品
            3. 通过设置最小提升度去除存在抑制关系的强关联规则, 即用户在买某商品时, 可能会继续购买的另外一个商品
        此次将强关联规则分为前件和后件两列数据呈现
"""
import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt


# 定义函数, 将字符串转换为包含单个字符串的列表
def conversion_data(stationery):
    return [stationery]


if __name__ == '__main__':
    # 读取源数据
    dataFrame = pd.read_csv(filepath_or_buffer='./文具市场购物篮案例练习/工作/StationeryOrder.csv', sep=',',
                            encoding='gbk', engine='python')
    # 将文具数据格式转换为包含单个字符串的列表
    dataFrame['stationery'] = dataFrame['stationery'].agg(conversion_data)
    # 分组聚合根据 id 合并文具为包含多个字符串的列表, 并重置索引
    dataFrame = dataFrame.groupby('id').sum().reset_index()
    # print(dataFrame)
    # 设置最小支持度、最小置信度以及最小提升度分别为: 0.02、0.45、1; 调用 apriori() 函数
    results = apriori(dataFrame['stationery'], min_support=0.02, min_confidence=0.45, min_lift=1)
    # 创建列表
    extract_result = []

    for result in results:
        # 获取支持度,并保留3位小数
        support = round(result.support, 3)

        # 遍历ordered_statistics对象
        for rule in result.ordered_statistics:
            # 获取前件和后件并转成列表
            head_set = list(rule.items_base)
            tail_set = list(rule.items_add)

            # 跳过前件为空的数据
            if not head_set:
                continue

            # 提取置信度，并保留3位小数
            confidence = round(rule.confidence, 3)
            # 提取提升度，并保留3位小数
            lift = round(rule.lift, 3)

            # 将提取的数据保存到提取列表中
            extract_result.append([head_set, tail_set, support, confidence, lift])
    # 将数据转化为 DataFrame 的格式
    result_dataFrame = pd.DataFrame(extract_result, columns=[
        '前件', '后件', '支持度', '置信度', '提升度'])
    # print(result_dataFrame)
    # 将“前件”、“后件”列转成字符串，方便后续提取数据
    result_dataFrame['前件'] = result_dataFrame['前件'].astype('str')
    result_dataFrame['后件'] = result_dataFrame['后件'].astype('str')
    # 提取后件中“中性笔”的数据
    gel_pens = result_dataFrame[result_dataFrame['后件'] == "['中性笔']"]
    print(gel_pens)
    # 按照“支持度”对提取的数据进行排序
    gel_pens = gel_pens.sort_values('支持度')
    # 获取重置后的索引
    df_index = gel_pens.reset_index().index
    # 设置柱子的宽度
    width = 0.2
    # 设置 x 的坐标值
    x = df_index
    x1 = x - width / 2
    x2 = x + width / 2
    # 设置 y 的坐标值
    y1 = gel_pens['支持度']
    y2 = gel_pens['置信度']
    # 设置字体
    plt.rcParams['font.family'] = ['KaiTi']
    # 设置画布尺寸
    plt.figure(figsize=(18, 10))
    # 绘制多组柱状图
    plt.bar(x1, y1, width=width)
    plt.bar(x2, y2, width=width)
    # 设置图表标题名及字体大小
    plt.title('“中性笔”对应前件的支持度、置信度数值比较', fontsize=20)
    # 设置 x 坐标轴的刻度
    plt.xticks(x, gel_pens['前件'])
    # 设置坐标轴的标题名及字体大小
    plt.xlabel('前件', fontsize=15)
    plt.ylabel('数值', fontsize=15)
    # 设置 y 轴的数值显示范围
    plt.ylim(0, 0.6)
    # 设置图例
    plt.legend(['支持度', '置信度'], fontsize=15)
    # 设置数据标签
    for a, b in zip(x1, y1):
        plt.text(a, b, str(round(b * 100, 1)) + '%', ha='center', va='bottom', fontsize=12)
    for a, b in zip(x2, y2):
        plt.text(a, b, str(round(b * 100, 1)) + '%', ha='center', va='bottom', fontsize=12)
    plt.show()
    # 保存处理好的数据到另一个文件
    dataFrame.to_csv('./文具市场购物篮案例练习/工作/StationeryOrder_clear.csv', encoding='gbk', index=False)
    result_dataFrame.to_csv('./文具市场购物篮案例练习/工作/result_data.csv', encoding='gbk', index=False)
