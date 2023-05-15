"""
    1. 数据的读取与写入
        读取Excel数据: read_excel()
            以DataFrame格式读取Excel数据, 并返回一个DataFrame对象
            语法:
                pd.read_excel(io, sheet_name):
                    参数:
                        io: excel文件路径
                        sheet_name: excel文件的工作表名称, 默认为第一个工作表
        将数据写入excel文件: to_excel()
            以DataFrame格式将数据写入到excel文件
            语法:
                df.to_excel(excel_writer, sheet_name, index):
                    参数:
                        excel_writer: Excel文件路径或文件对象
                        sheet_name: Excel文件的工作表名称, 默认为’Sheet1‘
                        index: 是否在写入的文件中加入行索引, 默认为True, 加入索引
    2. 数据的类型转换
        astype()函数:
            将series/DataFrame对象转换为指定的数据类型
            语法:
                s / df.astype(dtype)
                    参数:
                        dtype: 数据类型, 如int, str等
    3. 数据的批量替换
        replace()方法:
            对DataFrame对象中的数据实现批量替换操作
            语法:
                df.replace(to_replace):
                    参数:
                        to_replace:被替换的内容, 可以为字典
                        例:
                            transform_label = {3:'三'}
                            data.replace(transform_label)
                    只对某一列数据进行修改:
                        df['列名'] = df['列名'].replace(to_replace)

"""
import pandas as pd

'''excel文件数据读取'''
# # 读取excel文件数据
# data = pd.read_excel('./素材文件/工作/成绩单.xlsx', sheet_name='1 班')
# print(data)
# # 将DataFrame格式数据写入Excel文件
# data.to_excel('./素材文件/工作/test.xlsx', sheet_name='sheet2', index=False)

'''数据类型转换-astype()函数'''
# # 创建DataFrame对象
# data_2 = pd.DataFrame({'商品名': ['猪头皮', '醋', '高压锅'], '单价': [10, 13, 800], '数量': ['5', '2', '1']})
# # 打印data_2
# print(data_2)
# print('==============')
# # 修改‘数量’栏位的数据类型并添加总价列
# data_2['总额'] = data_2['单价'] * data_2['数量'].astype(int)
# # 打印data_2
# print(data_2)

'''数据批量替换'''
# 创建一个DataFrame对象
data_3 = pd.DataFrame({'性别': ['难', '女', '难', '女', '女'],
                       '城市': ['.', '潮州市', '山头市', '汕尾市', '山头市'],
                       '年龄': [25, 26, 24, 25, 26],
                       '爱好': ['蓝球', '跑步', '跳舞', '逛街', '读书']})
# 打印
print(data_3)
print('==============')
# 定义字典替换’山头市‘和’蓝球‘
transform_label = {
    '山头市': '汕头市',
    '蓝球': '篮球'
}
# data_3 = data_3.replace(transform_label)
# 只替换城市列数据
data_3['城市'] = data_3['城市'].replace(transform_label)
# 打印
print(data_3)
