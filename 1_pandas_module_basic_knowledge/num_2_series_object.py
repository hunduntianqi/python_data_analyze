"""
    Series:
        pandas中的一种数据结构, 主要有一组数据及其对应的索引组成
        Series对象左侧的是索引, 右侧的是数据 >> 索引:数据
        创建Series对象:
            pd.Series(data)方法:
                1. 根据列表创建Series对象:
                    默认索引: pd.Series(数据列表)
                    指定索引: ps.Series(数据列表, 索引列表)
                2. 根据字典创建Series对象--key为对应索引, value为对应的数据:
                    pd.Series(字典)
                3. 根据标量创建Series对象:
                    pd.Series(标量数据)
                4. 根据n维数组创建Series对象:
                    import numpy as np
                    pd.Series(np.array([1, 2]))
                5. 根据字符串创建Series对象
                    ps.Series(字符串数据)
            Series.index: 可以获取Series对象的索引数据
            Series.values: 可以获取Series对象的数据内容
"""
# 导入pandas库
import pandas as pd
# 导入numpy库
import numpy as np

# 根据列表创建Series对象, 默认索引-起始为0
serobj = pd.Series(['郭鹏涛', '陈欣妮', '郭会军', '任杏好', '郭鹏强'])
print(serobj.index)  # ==> RangeIndex(start=0, stop=5, step=1)
print(serobj.values)  # ==> ['郭鹏涛' '陈欣妮' '郭会军' '任杏好' '郭鹏强']
# 打印Series对象
print(serobj)
'''
    打印结果为:
        0    郭鹏涛
        1    陈欣妮
        2    郭会军
        3    任杏好
        4    郭鹏强
'''
print('==================================')
# 根据列表创建Series对象, 指定索引-可指定索引为任意类型
serobj_index = pd.Series(['郭鹏涛', '陈欣妮', '郭会军', '任杏好', '郭鹏强'], index=['24', '24', '48', '47', '21'])
# 打印Series对象
print(serobj_index)
'''
    打印结果为:
        24    郭鹏涛
        24    陈欣妮
        48    郭会军
        47    任杏好
        21    郭鹏强
        dtype: object
'''
print('==================================')
# 根据字典创建Series对象
ser_dic = pd.Series({'1月': 109, '2月': 129, '3月': 158})
# 打印
print(ser_dic)
'''
    打印结果为:
        1月    109
        2月    129
        3月    158
        dtype: int64
'''
print('==================================')
# 根据标量创建Series对象
ser_scalar = pd.Series(5, index=[1])
# 打印
print(ser_scalar)
'''
    打印结果为:
        1    5
        dtype: int64
'''
print('==================================')
# 根据n维数组创建对象
ser_arr = pd.Series(np.array([1, 2, 3, '数组']), index=[1, 2, 3, 4])
print(ser_arr)
'''
    打印结果为:
        1     1
        2     2
        3     3
        4    数组
        dtype: object 
'''
print('==================================')
# 根据字符串创建Series对象
ser_str = pd.Series('hello', index=[1])
print(ser_str)
'''
    打印结果为:
        1    hello
        dtype: object
'''
