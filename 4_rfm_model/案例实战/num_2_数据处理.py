"""
    数据处理:
        1. 数据清洗: 对数据的缺失值, 重复值, 异常值进行清洗
        2. 数据整理: 删除无关数据, 提取与RFM模型相关的重要数据
            * 新增一个商品总额列, 计算每个商品的消费总额
            * 将商品按照订单号进行分组, 合并商品总额, 得到用户每个订单的消费金额
            * 只保留计算RFM所需要的数据-订单号, 用户ID, 发货日期, 总金额
            * 计算R(用户所有订单中时间差最小的值), F(用户消费订单的总数量), M(计算用户所有消费订单的总额)
"""
import pandas as pd

'''数据清洗'''
data = pd.read_excel('../素材文件/工作/商品销售数据.xlsx')
# 查看缺失值
print(data.isna())
# 删除缺失值
data = data.dropna()
# 删除重复值
data = data.drop_duplicates()
# 查看异常值
print(data.describe())
# 布尔索引删除异常值
data = data[data['数量'] >= 0].reset_index(drop=True)
print(data.info())
print(data)

'''数据整理'''
# 新增商品总额列
data['商品总额'] = data['数量'] * data['价格']
# 将商品按照订单号分组, 合并商品总额, 并保留RFM所需要的数据
data = data.groupby(['订单号', '用户 ID'], as_index=False).agg({'发货日期': 'max', '商品总额': 'sum'})
print(data)
# 设定当前时间
today = '2012-01-01 00:00:00'
# 计算时间差
data['时间间隔'] = (pd.to_datetime(today) - pd.to_datetime(data['发货日期'])).dt.days
# # 筛选最小时间差
# data_R = data.groupby('用户 ID')['时间间隔'].min()
# print(data)
# print(data_R)
# # 计算 M 值
# # 汇总用户的订单消费总额
# data_M = data.groupby('用户 ID', as_index=False).agg({'商品总额': 'sum'})
# print(data_M)
# # 计算 F 的值
# # 统计用户的订单总数
# data_F = data.groupby('用户 ID', as_index=False).agg({'订单号': 'count'})
# print(data_F)

# 计算 R, F, M的值
rfm_data = data.groupby('用户 ID', as_index=False).agg({
    '时间间隔': 'min',
    '订单号': 'count',
    '商品总额': 'sum'
})
print(rfm_data)
# 重置列名
rfm_data.columns = ['用户id', '最小时间间隔(R)', '订单数量(F)', '消费总额(M)']
print(rfm_data)
# 对数据进行排序
rfm_data = rfm_data.sort_values(by='最小时间间隔(R)')
rfm_data = rfm_data.sort_values(by='订单数量(F)', ascending=False)
rfm_data = rfm_data.sort_values(by='消费总额(M)', ascending=False)
# 保存整理后的数据
rfm_data.to_excel('../素材文件/工作/商品销售数据-clean.xlsx', index=False)
