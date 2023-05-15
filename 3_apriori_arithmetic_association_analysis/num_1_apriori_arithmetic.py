"""
    Apriori算法-关联分析:
        基础知识:
            抽取案例所需的python基础知识, 进行针对性讲解
            1. 修改列名:
                以字典创建DataFrame对象时, 字典的键为列名, 值作为行数据
                以嵌套列表创建DataFrame对象时, 列表的元素会作为行数据显示, 数据的列名默认从0开始
                在使用列表创建DataFrame对象时, 可以借助参数columns来设置列名
                修改列名:
                    DataFrame.columns=['列名1', '列名2', '列名3', ...]
            2. 数据排序:
                sort_values(by, ascending, na_position)方法:对指定列进行排序操作, 默认为升序
                    by: 排序的列名
                    ascending: 排序方式, 默认为升序-True, 降序为False
                    na_position: 如果排序的数据中有Nan值, 指定Nan值放在最后一个还是第一个, 默认为last, 最后一个, first-第一个
                DataFrame对象:df.sort_values(by='列名')
                Series对象: s.sort_values()
            3. 重置索引:
                reset_index()方法:
                    s / df.reset_index(drop=False):
                        drop:
                            False: 保留原索引, 默认值
                            True: 不保留原索引
            4. 数值的四舍五入:
                round()函数:
                    round(number, ndigits=0)
                        number: 要四舍五入计算的数列
                        ndigits: 要保留的小数位, 默认为0位
            5. agg(func)方法:
                对一组数据进行某函数处理
                func: 自定义函数名称, 传入函数时, 只需要写上函数名, 不需要加上括号和函数参数
                例: data['库存'].agg(func)
        分析方法-关联分析:
            介绍案例所需的分析方法及其核心知识
            关联分析:
                用于发现大量数据之中, 各组数据之间的联系
                1. 事务: 每一条交易数据可以称为一个事务
                2. 项: 指交易中的物品, 不同物品可以称为一个项
                3. 项集: 0个或多个项组成的集合, k个项组成的集合叫k项集
                4. 支持度: 指项集在所有事务中出现的次数比例
                    support(x) = 项集{x}出现次数 / 事务总次数
                5. 频繁项集:
                    指人为设定一个最小支持度, 支持度大于或等于最小支持度的项集称为频繁项集
                6. 关联规则:
                    指数据之间的联系, 表达式为: {x} -> {y}, x和y之间不存在相同项
                    项集{x}: 前件
                    项集{u}: 后件
                    关联规则含义: 指购买物品x和购买物品y之间可能存在某种联系
                7. 置信度: 用于衡量关联规则的可靠程度, 表示在前件出现的情况下, 后件出现的概率, 一般概率越高, 规则的可靠性越强
                    关联规则{x} -> {y}的置信度 = 项集{x, y}的支持度 / 项集{x}的支持度
                8. 强关联规则:
                    指人为设定最小置信度, 置信度大于或等于最小置信度的关联规则
                9. 提升度:
                    指一个项集的出现, 对另一个项集的出现影响有多大
                    {x} -> {y}的提升度 = {x} -> {y}的置信度 / {y}的支持度 ==> 指x的出现对y出现的影响有多大
                    提升度小于1: 表示前件对后件是抑制关系
                    提升度大于1: 表示前件对后件是促进关系
                    提升度等于1: 表示前件不影响后件, 两者之间没有关系
            Apriori算法流程步骤:
                1. 确定最小支持度和最小置信度
                    1.1 根据经验进行设置
                    1.2 试错法, 根据频繁项集和关联规则的结果倒推
                    1.3 其他方法...
                2. 找出所有频繁项集和强关联规则
                    2.1 频繁项集:
                        2.1.1: 一个项集如果是频繁的, 那它的非空子集也一定是频繁的
                        2.1.2: 一个项集如果是非频繁的, 那包含该项集的项集也一定是非频繁的
                3. apriori函数:
                    python第三方库apriori模块下的函数
                    功能: 执行apriori算法, 并返回包含关联规则的数据(为生成器对象, 可以通过遍历取出数据)
                    apriori(transactions, min_support, min_confidence, min_lift):
                    返回一个包含关联规则的生成器对象
                    参数:
                        transactions: 事务的集合, 值可以是嵌套列表或者Series对象
                        min_support: 最小支持度, 默认值为0.1
                        min_confidence: 最小置信度, 默认值为0.0
                        min_lift: 最小提升度, 默认值为0.0
        案例实战:
            结合基础知识和数据分析分析方法, 解决具体的案例问题
"""
# 导入 apyori 模块下的 apriori 函数
from apyori import apriori

# 创建4条快餐交易数据
orders = [['薯条', '可乐'], ['薯条', '可乐', '奶茶'], ['汉堡', '薯条', '可乐'], ['汉堡', '可乐']]
# 创建变量 results，调用 apriori 函数，传入参数：orders，最小支持度为 0.2，最小置信度为 0.7
results = apriori(orders, min_support=0.2, min_confidence=0.7)
# 查看变量 results ==> 生成器对象
print(results)
# 遍历results
for result in results:
    print(result)
    # 获取支持度,并保留3位小数
    support = round(result.support, 3)

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
        # 查看强关联规则，支持度，置信度，提升度
        print(related_catogory, support, confidence, lift)
