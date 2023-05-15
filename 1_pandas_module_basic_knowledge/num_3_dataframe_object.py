"""
    DataFrame对象:
        是一种表格型的数据结构, 包含行索引、列索引以及一组数据
        行索引: 对应行数, 默认从0开始
        列索引: 类似于表格的表头, 可自定义
        数据: 由行索引和列索引包裹定位的每个表格
        创建DataFrame对象:
            方法: pd.DataFrame(data)
            1. 根据字典创建DataFrame对象:
                pd.DataFrame(字典)
                注意: 根据字典创建DataFrame对象时, 每个key对应的数据个数必须相等, 使用字典创建的Dataframe对象
                      中, 列名为对应的key, value为每一列数据, 行索引默认从0开始依次递增
            2. 根据多维数组创建DataFrame对象:
                例:
                    class_df2 = pd.DataFrame(np.array([[25, '女'],  # 数据
                                   [18, '女'],  # 数据
                                   [23, '女'],  # 数据
                                   [18, '男']]),  # 数据
                         columns=['年龄', '性别'],  # 表头
                         index=[1, 2, 3, 4]  # 指定行索引
                         )

"""
# 导入pandas库
import pandas as pd
# 导入numpy库
import numpy as np

# 根据字典创建DataFrame对象
dataframe_dict = pd.DataFrame({'年龄': [23, 22, 21], '岗位': ['客服', '运营', '公关'], '年购买量': [10, 15, 8]})
# 打印dataframe对象
print(dataframe_dict)
'''
    打印结果为:
           年龄  岗位  年购买量  # 列名
        0  23  客服    10 # 数据
        1  22  运营    15 # 数据
        2  21  公关     8 # 数据
      行索引
'''
print('==============================')
# 指定行索引创建DataFrame对象
dataframe_dict_index = pd.DataFrame({'年龄': [23, 22, 21],
                                     '岗位': ['客服', '运营', '公关'],
                                     '年购买量': [10, 15, 8]},
                                    index=[1, 2, 3])
# 打印dataframe对象
print(dataframe_dict_index)
'''
    打印结果为:
           年龄  岗位  年购买量  # 列索引
        1  23  客服    10 # 数据
        2  22  运营    15 # 数据
        3  21  公关     8 # 数据
      行索引
'''
print('==============================')
# 根据多维数组创建DataFrame对象
dataframe_array = pd.DataFrame(np.array([[25, '女'],  # 数据
                                         [18, '女'],  # 数据
                                         [23, '女'],  # 数据
                                         [18, '男']]),  # 数据
                               columns=['年龄', '性别'],  # 表头
                               index=[1, 2, 3, 4]  # 指定行索引
                               )
# 打印DataFrame对象年龄一列数据
print(dataframe_array['年龄'])
