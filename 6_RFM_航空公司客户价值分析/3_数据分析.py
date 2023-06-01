import pandas as pd
import matplotlib.pyplot as plt


# 定义函数按照区间划分标记 R 值
def caculate_r(s):
    if s <= 140:
        return 5
    elif s <= 280:
        return 4
    elif s <= 420:
        return 3
    elif s <= 560:
        return 2
    else:
        return 1


# 定义函数按照区间划分标记 F 值
def caculate_f(s):
    if s <= 4:
        return 1
    elif s <= 7:
        return 2
    elif s <= 10:
        return 3
    elif s <= 20:
        return 4
    else:
        return 5


# 定义函数按照区间划分标记 M 值
def caculate_m(s):
    if s <= 5000:
        return 1
    elif s <= 10000:
        return 2
    elif s <= 15000:
        return 3
    elif s <= 20000:
        return 4
    else:
        return 5


if __name__ == '__main__':
    # 读取数据
    dataFrame = pd.read_excel('./案例素材/clean_dfile.xlsx')
    # 绘制 R 值的分值区间
    plt.figure(figsize=(6, 6))
    x = dataFrame['最近一次间隔天数'].sort_values()
    y = dataFrame.index
    plt.plot(x, y)
    # plt.show()
    # 标记 R 值
    dataFrame['R评分'] = dataFrame['最近一次间隔天数'].agg(caculate_r)
    # 查看数据的前 10 行信息
    print(dataFrame.head(10))
    # 绘制 F 值的分值区间
    plt.figure(figsize=(6, 6))
    x = dataFrame['近2年乘机次数'].sort_values()
    y = dataFrame.index
    plt.plot(x, y)
    # plt.show()
    # 标记 F 值
    dataFrame['F评分'] = dataFrame['近2年乘机次数'].agg(caculate_f)
    # 绘制 M 值的分值区间
    plt.figure(figsize=(6, 6))
    x = dataFrame['近2年乘机金额'].sort_values()
    y = dataFrame.index
    plt.plot(x, y)
    # 标记 M 值
    dataFrame['M评分'] = dataFrame['近2年乘机金额'].agg(caculate_m)
    # 计算R评分、F评分、M评分的平均数
    r_avg = dataFrame['R评分'].mean()
    f_avg = dataFrame['F评分'].mean()
    m_avg = dataFrame['M评分'].mean()
    print('R评分的均值为：{}，F评分的均值为{},M评分的均值为{}'.format(r_avg, f_avg, m_avg))

    # 将R评分、F评分、M评分 的数据分别与对应的平均数做比较
    dataFrame['R评分'] = (dataFrame['R评分'] > r_avg) * 1
    dataFrame['F评分'] = (dataFrame['F评分'] > f_avg) * 1
    dataFrame['M评分'] = (dataFrame['M评分'] > m_avg) * 1

    # 拼接R评分、F评分、M评分
    rfm_score = dataFrame['R评分'].astype(str) + dataFrame['F评分'].astype(str) + dataFrame['M评分'].astype(str)

    # 定义字典标记 RFM 评分档对应的用户分类名称
    transform_label = {
        '111': '重要价值用户',
        '101': '重要发展用户',
        '011': '重要保持用户',
        '001': '重要挽留用户',
        '110': '一般价值用户',
        '100': '一般发展用户',
        '010': '一般保持用户',
        '000': '一般挽留用户'
    }
    # 将RFM评分替换成具体的客户类型
    dataFrame['客户类型'] = rfm_score.replace(transform_label)
    print(dataFrame)
    # 可视化客户类型的分布
    customer_data = dataFrame.groupby('客户类型')['会员卡号'].count()
    # plt 设置中文显示字体
    plt.rcParams['font.family'] = ['KaiTi']
    plt.figure(figsize=(10, 10))
    plt.bar(customer_data.index, customer_data)
    plt.xlabel('客户类型', fontsize=12)
    plt.ylabel('人数', fontsize=12)
    plt.title('不同客户的数量分布', fontsize=16)
    plt.show()
