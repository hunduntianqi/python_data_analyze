"""
    数据分析:
        执行 Apriori 算法需要设置的参数包括数据集、最小支持度、最小置信度以及最小提升度
            1. 通过设置最小支持度筛选频繁项集, 即用户更有可能购买的商品
            2. 通过设置最小置信度筛选强关联规则, 即用户在购买某商品时, 更倾向于或更不倾向于购买的另外一个商品
            3. 通过设置最小提升度去除存在抑制关系的强关联规则, 即用户在买某商品时, 可能会继续购买的另外一个商品
"""