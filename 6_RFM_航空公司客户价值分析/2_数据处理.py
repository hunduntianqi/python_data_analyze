import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 读取数据, 获取DataFrame对象
    dataFrame = pd.read_excel('./案例素材/air_new_data.xlsx')
    # 查看数据是否存在空值
    print(dataFrame.isna())
    # 去除“最近一次间隔天数”为空的记录
    data_notnull = dataFrame.dropna(subset=['最近一次间隔天数'])
    # 去除"近两年乘机次数"为空的记录
    data_notnull = data_notnull.dropna(subset=['近2年乘机次数'])
    # 去除"消费金额"为空的记录
    data_notnull = data_notnull.dropna(subset=['消费总金额'])
    # 查看处理后数据基本信息
    # print(data_notnull.info())
    # 查看数据是否有重复值
    print(data_notnull.duplicated())  # 数据无重复值
    # 查看数据描述性统计信息
    print(data_notnull.describe())
    # 只保留消费金额非零的记录，同时去除年龄大于 100 的记录
    data_notnull = data_notnull[data_notnull['消费总金额'] != 0]
    data_notnull = data_notnull[data_notnull['年龄'] <= 100]
    # 关键字段提取
    data_notnull = data_notnull[['会员卡号', '最近一次间隔天数', '近2年乘机次数', '近2年乘机金额']]
    # 保存清洗后的数据
    data_notnull.to_excel('./案例素材/clean_dfile.xlsx', index=False)