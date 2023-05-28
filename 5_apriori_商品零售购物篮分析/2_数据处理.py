"""
    本次案例分析的是顾客在 '一次购买行为' 中放入 '购物篮' 的 '不同商品之间的关联', 因此适合 Apriori 算法计算的数据形式为:
        按照 'id' 进行分组聚合的 '文具' 数据
    数据处理:
        思路: 文具列数据由字符串转换成列表
            1. 先将"字符串"格式的文具列数据转换为"包含单个字符串的列表"格式
            2. 使用 df.groupby().sum()将同一 id 的 "包含单个字符串列表"数据聚合为"包含多个字符串列表"格式的数据
"""
import pandas as pd


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
    print(dataFrame)
    # 保存处理好的数据到另一个文件
    dataFrame.to_csv('./文具市场购物篮案例练习/工作/StationeryOrder_clear.csv', encoding='gbk', index=False)
