"""
    目标: 基于 RFM 的阈值, 对用户进行分类
        计算 RFM 阈值:
            本案例中, 在和电商运营人员商讨中发现, 如果直接通过平均值或中位数进行阈值的划分不够客观, 因为不同的客户对于电话推送优惠活动的反应不同
            因此, 我们需要选择更加灵活的阈值计算方式: 分区域评分, 计算平均值; 计算流程为:
                划分区间 —— 标记分数 —— 计算平均值:
                    划分区间:
                        a. 确认关键的节点进行划分
                        b. 根据实际经验进行划分
                    标记分数:
                        根据不同的区间, 标记不同的分数
                    计算平均值:
                        将 R, F, M盒子各自划分好区间并标记分数后, 根据标记的分数计算平均值
            得到 R, F, M平均值, 以平均值为阈值, 将RFM各值进行高低值标记, 并划分用户类型:
                1. 将获得的阈值与 RFM 分数进行比较，高于阈值记为“高”，低于阈值记为“低”, 高低值可暂时用 1 和 0 表示
                2. 根据标记, 将用户分为 000, 001, 010, 100, 011, ....等类型
                3. 根据用户分类对照表创建映射字典 ==> dict_map
                4. 根据replace()方法, 传入映射字典, 批量修改用户类型
                    dataFrame['user_type'] = dataFrame['user_score'].replace(dict_map)
                    也可以使用df.map()方法批量替换数据, 使用时与agg()方法类似, 要先定义函数
            分组聚合获取用户数量状况, 并画出柱状图或饼状图展示出来
                user_count = dataFrame.groupby('用户分类')['用户id'].count()
                绘制图表:
                    # 绘制柱状图, 展示用户类型分布
                        plt.figure(figsize=(12, 8))
                        plt.bar(user_count.index, user_count)
                        plt.xlabel('客户类型', fontsize=12)
                        plt.ylabel('人数', fontsize=12)
                        plt.title('不同客户的数量分布', fontsize=16)
                    # 绘制饼图, 显示用户类型分布
                        plt.figure(figsize=(14, 10))
                        plt.pie(user_count, labels=user_count.index, autopct='%0.1f%%')
                        plt.title('不同客户占比情况', fontsize=16)
"""
import pandas as pd
import matplotlib.pyplot as plt


# 根据最小时间间隔折线图, 定义函数划分评分区间
def interval_divide_recency(recency):
    """ 根据 R 值折线图可知, 大于400天曲线平缓, 几乎没有变化, 小于400天曲线变化均匀 """
    # 小于400天以100天为一个区间, 大于400天为一个区间
    if recency <= 100:
        return 5
    elif 100 < recency <= 200:
        return 4
    elif 200 < recency <= 300:
        return 3
    elif 300 < recency <= 400:
        return 2
    else:
        return 1


# 根据订单总额折线图, 定义函数划分评分区间
def interval_divide_frequency(frequency):
    """ 根据 F 值折线图可知, 曲线大约以 20 次为界限, 20 之前的呈曲线分布, 20 后的几乎呈直线分布 """
    # 小于20以5次为一个区间, 大于20次为一个区间
    if frequency <= 5:
        return 1
    elif 5 < frequency <= 10:
        return 2
    elif 10 < frequency <= 15:
        return 3
    elif 15 < frequency <= 20:
        return 4
    else:
        return 5


# 根据消费总额折线图, 定义函数划分评分区间
def interval_divide_money(money):
    """ 根据 M 值折线图可知, 曲线大约以 8000 元为界限, 8000 之前的呈曲线分布, 8000 后的几乎呈直线分布 """
    # 小于8000以2000为一个区间, 大于8000为一个区间
    if money <= 2000:
        return 1
    elif 2000 < money <= 4000:
        return 2
    elif 4000 < money <= 6000:
        return 3
    elif 6000 < money <= 8000:
        return 4
    else:
        return 5


# 定义函数, 根据 R, F, M高低值与用户分类规则表进行用户分类
def user_classify(rfm):
    if rfm == "000":
        return "一般挽留用户"
    elif rfm == "010":
        return "一般保持用户"
    elif rfm == "100":
        return "一般发展用户"
    elif rfm == "110":
        return "一般价值用户"
    elif rfm == "001":
        return "重要挽留用户"
    elif rfm == "011":
        return "重要保持用户"
    elif rfm == "101":
        return "重要发展用户"
    elif rfm == "111":
        return "重要价值用户"


if __name__ == '__main__':
    # plt 设置中文显示字体
    plt.rcParams['font.family'] = ['KaiTi']
    # 设置折线图画布
    plt.figure(figsize=(10, 8))
    # 读取数据, 获取DataFrame对象
    dataFrame = pd.read_excel('../素材文件/工作/商品销售数据-clean.xlsx')
    # 准备数据, 确定x, y轴数据, 画出 R 值折线图
    x_R = dataFrame['最小时间间隔(R)'].sort_values()
    y = dataFrame.index
    # 最小时间间隔数据加入画布, 绘制图形
    plt.plot(x_R, y)
    # 图表展现
    # plt.show()
    # 新建 R评分 列, 调用函数为最小时间间隔评分
    dataFrame['R评分'] = dataFrame['最小时间间隔(R)'].agg(interval_divide_recency)
    # 准备数据, 确定x, y轴数据, 画出 F 值折线图
    # 设置折线图画布
    plt.figure(figsize=(10, 8))
    x_F = dataFrame['订单数量(F)'].sort_values()
    # 订单数量数据加入画布, 绘制图形
    plt.plot(x_F, y)
    # 图表展现
    # plt.show()
    # 新建 F评分 列, 调用函数为订单数量评分
    dataFrame['F评分'] = dataFrame['订单数量(F)'].agg(interval_divide_frequency)
    # 设置折线图画布
    plt.figure(figsize=(10, 8))
    x_M = dataFrame['消费总额(M)'].sort_values()
    # 消费总额数据加入画布, 绘制图形
    plt.plot(x_M, y)
    # 图表展现
    # plt.show()
    # 新建 M 评分 列, 调用函数为消费总额评分
    dataFrame['M评分'] = dataFrame['消费总额(M)'].agg(interval_divide_money)
    # print(dataFrame)
    # 计算R, F, M各参数的评分平均值
    r_average = dataFrame['R评分'].mean()
    f_average = dataFrame['F评分'].mean()
    m_average = dataFrame['M评分'].mean()
    print('R评分的均值为：{}，F评分的均值为{},M评分的均值为{}'.format(r_average, f_average, m_average))
    # 为 R, F, M评分标记高低值
    dataFrame['R_高低值判断'] = (dataFrame['R评分'] > r_average) * 1
    dataFrame['F_高低值判断'] = (dataFrame['F评分'] > f_average) * 1
    dataFrame['M_高低值判断'] = (dataFrame['M评分'] > m_average) * 1
    # 高低值标记后, 根据用户分类规则表对用户进行分类, 标记用户类型
    # 将各评分列数据转换为字符串类型并拼接
    dataFrame_score = dataFrame['R_高低值判断'].astype(str) + dataFrame['F_高低值判断'] \
        .astype(str) + dataFrame['M_高低值判断'].astype(str)
    dataFrame['用户权重'] = dataFrame_score
    # 根据用户权重为用户分类
    # 定义字典, 指定映射关系
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
    dataFrame['用户分类'] = dataFrame['用户权重'].replace(transform_label)
    # 使用分组聚合操作, 获取每类用户数量信息
    user_count = dataFrame.groupby('用户分类')['用户id'].count()
    print(user_count)
    # 绘制柱状图, 展示用户类型分布
    plt.figure(figsize=(12, 8))
    plt.bar(user_count.index, user_count)
    plt.xlabel('客户类型', fontsize=12)
    plt.ylabel('人数', fontsize=12)
    plt.title('不同客户的数量分布', fontsize=16)
    # 绘制饼图, 显示用户类型分布
    plt.figure(figsize=(14, 10))
    plt.pie(user_count, labels=user_count.index, autopct='%0.1f%%')
    plt.title('不同客户占比情况', fontsize=16)
    plt.show()
    # 保存处理数据后文件
    dataFrame.to_excel('../素材文件/工作/商品销售数据-deal with.xlsx', index=False)
