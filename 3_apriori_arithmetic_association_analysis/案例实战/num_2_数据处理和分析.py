"""
    数据处理-获取可以进行关联分析的用户数据:
        1. 清洗数据:
            查找并清洗缺失值, 重复值, 异常值
        2. 整理数据:
            删除无关数据, 整理用户的阅读事务
    数据分析:
        1. 确定最小支持度和最小置信度
        2. 调用apriori函数获取强关联规则
"""

import pandas as pd
from apyori import apriori

'''=============数据处理==========='''
data = pd.read_csv(filepath_or_buffer='./需求数据/公众号用户访问数据.csv', sep=',', encoding='gbk', engine='python')
# print(data)
# 提取数据
data = data[['用户编号', '访问日期', '文章类别']]
# print(data)
# 查看重复值
# print(data.duplicated())
# 删除重复值
data = data.drop_duplicates()

# 转换数据类型
# 定义函数 >> 将字符串转换为列表, 便于数据处理
def conversion(category):
    # if str(category)[0] == '[':
    #     # category是列表, 不需要转换
    #     return category
    return [category]


# 调用agg函数转换文章类别为列表数据
data['文章类别'] = data['文章类别'].agg(conversion)
print(data)
# 分组查询处理数据
data = data.groupby(['访问日期', '用户编号'])['文章类别'].sum()
print(data)

'''=================数据分析================'''
"""
    观察数据可知: 用户总数和事务总数都为99, 且数据均为2020年9月份数据
    假设对访问频繁的文章组合要求为: 至少三天访问一次, 则事件发生的概率为: 30 / 3 / 99 = 0.1
    最小置信度暂无头绪, 先使用函数默认值
"""
min_support = 30 / 3 / 99
# 调用apriori函数
results = apriori(data.values, min_support=0.1, min_confidence=0.3)
# 创建列表存储打印数据
extract_result = []
for result in results:
    print(result)
    # 获取支持度, 并保留三位小数
    support = round(result.support, 3)
    print(support)
    # 遍历ordered_statistics对象
    for rule in result.ordered_statistics:
        # 获取前件和后件并转成列表
        head_set = list(rule.items_base)
        tail_set = list(rule.items_add)
        # 跳过前件为空的数据
        if head_set == []:
            continue
        # 将前件、后件拼接成关联规则的形式
        related_catogory = str(head_set) + '→' + str(tail_set)
        # 提取置信度，并保留3位小数
        confidence = round(rule.confidence, 3)
        # 提取提升度，并保留3位小数
        lift = round(rule.lift, 3)
        # # 查看强关联规则，支持度，置信度，提升度
        # print(related_catogory, support, confidence, lift)
        # 将打印数据添加到列表
        extract_result.append([related_catogory, support, confidence, lift])
# 根据嵌套列表创建DataFrame对象
rules_data = pd.DataFrame(extract_result)
# 为DataFrame对象修改列名
rules_data.columns = ['关联规则', '支持度', '置信度', '提升度']
# 根据支持度将数据进行升序排序
rules_data_sort = rules_data.sort_values(by='支持度')
# 提取提升度大于1的数据
rules_data_sort = rules_data_sort.sort_values(by='提升度', ascending=False)
rules_data_sort = rules_data_sort.reset_index(drop=True)
print(rules_data_sort.reset_index(drop=True))
# 将处理好的数据写入文件保存
rules_data_sort.to_csv('./需求数据/公众号用户访问数据-强关联规则.csv', encoding='gbk', index=False)
