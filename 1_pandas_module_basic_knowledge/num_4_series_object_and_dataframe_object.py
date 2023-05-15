"""
    Series对象和DataFrame对象的联系:
            >> DataFrame 对象可以被看作是由Series对象所组成的!!
            可以通过DataFrame[列索引]取出DataFrame对象中的一列数据
"""
# 导入pandas库
import pandas as pd
# 导入numpy库
import numpy as np

# 使用多维数组创建DataFrame对象
class_df2 = pd.DataFrame(np.array([['陈欣妮', 24, '女'],  # 数据
                                   ['任杏好', 47, '女'],  # 数据
                                   ['郭鹏涛', 18, '男']]),  # 数据
                         columns=['姓名', '年龄', '性别'],  # 表头
                         index=[1, 2, 3]  # 指定行索引
                         )
# 打印DataFrame对象
print(class_df2)
print('=============================')
# 使用列索引取出姓名一列数据
data = class_df2['姓名']
# 打印
print(data)
'''
    打印结果为:
        1    陈欣妮
        2    任杏好
        3    郭鹏涛
        Name: 姓名, dtype: object
'''

# 打印查看data数据类型
print(type(data))  # <class 'pandas.core.series.Series'>
