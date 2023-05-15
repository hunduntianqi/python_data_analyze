"""
    数据处理:
        1. 数据清洗:
            1.1 处理缺失值:
                在实际分析过程中, 会遇见数据统计不完整的情况, 一般将这些缺失的数据称为缺失值
                DatFrame.info()方法:
                    可以帮助我们提炼出DataFrame对象的基本数据信息, 其中包括:整体数据的总行数、
                    各列数据类型统计、各列的列名、各列总共有多少非空数据、表格占用的系统空间等
                1.1.1 查找缺失值:
                    在pandas库中, 可以使用isna()方法来查找DataFrame对象和Series对象中的缺失值,
                    该方法将查找结果以 DataFrame 对象或者 Series 对象的形式进行返回, 返回对象中
                    的内容都是布尔值, 缺失数据会用 True 来表示, False 则代表这里的数据不缺失
                    DataFrame.head()方法: 默认可以查看数据的前 5 行
                    DataFrame.tail()方法: 默认可以查看数据的后 5 行
                    pandas 库中，NaN 代表的就是缺失数据
                1.1.2 删除缺失值:
                    在pandas库中, 使用dropna()方法可以直接删除DataFrame对象和Series对象中的缺失值数据
                    在本案例中, 由于缺失值数据较少, 删除后不影响整体分析, 可以直接删除含有缺失值数据的行
                    注意: 该方法不会改变原来DataFrame对象的值, 会返回一个新的DataFrame对象
                    指定列索引删除缺失值:
                        DataFrame.dropna(subset=[列索引1, 列索引2, ...])
                1.1.3 填充缺失值:
                    DataFrame对象和Series对象都可以使用fillna()的方法给缺失值填充数据
                        语法:
                            DataFrame['列名'].fillna('要填充的数据')
            1.2 处理重复值:
                1.2.1 查找重复值:
                    duplicated()方法:
                        该方法会返回一个Series对象, 找出所有的重复值, 重复为True, 不重复为False
                        需要查看重复数据:DataFrame[DataFrame.duplicated()]
                1.2.2 删除重复值:
                    drop_duplicates()方法:
                        该方法会直接删除DataFrame对象中重复出现的整行数据(但不会删除第一次出现的数据)
            1.3 处理异常值:
                异常值: 指超出数据实际限定范围的值
                1.3.1 检查异常值:
                    describe()方法:
                        可以查看 Series 对象或者 DataFrame 对象的描述性统计信息
                        该方法返回的统计信息分别代表数值型数据的频数统计、平均值、标准差、最小值、第一四分位数、
                        中位数、第三四分位数以及最大值
                1.3.2 抽取数据范围:
                    布尔索引: 对数据进行筛选, 通过DataFrame[DataFrame[列索引] 条件表达式]的方法筛选需要的数据
                    其中DataFrame[列索引] 条件表达式会对DataFrame中的数据进行逐行运算, 返回一个Series对象, 该对象的
                    数据为布尔值
        2. 数据整理
            指在数据分析前对所需字段进行数据排序、数据转换、数据抽取、数据合并、数据计算等准备操作
            字段: 指表格的列, 在本案例中包括: '订单编号'、'日期'、'省'……等字段
            转换日期数据:
                在本案例中, 需要先对每月的数据进行分析, 所以需要将日期由每一天转换为月份并插入数据, 该数据中的日期并不是日期格式,
            而是字符串格式, 所以需要先对日期数据进行转换
                pd.to_datetime(arg, format)方法:
                    可以将DataFrame或Series中的数据类型转换为datetime类型
                    arg: 要转换的数据, 可以是DataFrame或Series对象
                    format: 指datatime类型的日期格式, 比如该案例中这份数据,
                            它是以年-月-日的形式出现的，那么它对应的 format 就是 '%Y-%m-%d'（year-month-day的缩写
            提取月份信息:
                Series.dt方法:
                    可以把datatime类型的数据转换成一种方便提取日期或时间的对象, 该对象包含有year(年), month(月), day(日)等多种属性
                    可以通过 Series.dt.year、Series.dt.month 以及 Series.dt.day 来获取数据的年、月、日的信息
            添加新列:
                方法: DataFrame['colname'] = Series >> 为原数据添加新的一列
                    colname: 列名
                    Series: 要添加的数据, 为Series对象
        3. 数据写入:
            DataFrame.to_csv(path, encoding, index)
                path: 要保存文件的路径
                encoding: 保存文件的编码格式
                index: 是否写入行索引, 默认为True, 表示写入, False表示不写入
"""
# 导入pandas库
import pandas as pd

# 读取数据csv文件
mask_data = pd.read_csv(filepath_or_buffer='./需求数据/mask_data.csv', sep=';', encoding='utf-8', engine='python')
# print(mask_data)
# 使用info()方法查看mask_data对象的基本信息
print(mask_data.info())
'''
    打印结果为:
        <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 101942 entries, 0 to 101941
        Data columns (total 6 columns):
         #   Column  Non-Null Count   Dtype  
        ---  ------  --------------   -----  
         0   订单编号    101942 non-null  object 
         1   日期      100956 non-null  object  # 非空数据少
         2   省       100956 non-null  object  # 非空数据少
         3   订单量     100960 non-null  float64 # 非空数据少
         4   单价      100958 non-null  float64 # 非空数据少
         5   销售额     100960 non-null  float64 # 非空数据少
        dtypes: float64(3), object(3)
        memory usage: 4.7+ MB
        None
'''
# 使用isna()方法查找缺失值
print(mask_data.isna())
'''
    打印结果为:
                 订单编号     日期      省    订单量     单价    销售额
        0       False  False  False  False  False  False
        1       False  False  False  False  False  False
        2       False  False  False  False  False  False
        3       False  False  False  False  False  False
        4       False  False  False  False  False  False
        ...       ...    ...    ...    ...    ...    ...
        101937  False   True   True   True   True   True
        101938  False   True   True  False  False  False
        101939  False   True   True  False  False  False
        101940  False   True   True  False   True  False
        101941  False   True   True  False   True  False
'''
# 使用dropna()方法删除含有缺失值行的数据
mask_data = mask_data.dropna()
# 使用tail方法查看数据后五行
print(mask_data.tail())
'''
    打印结果为:
                                       订单编号          日期   省   订单量    单价    销售额
            0       87af-48e5-8bed-c5dcf9ecc172  2020-01-01  广东   0.0  30.0    0.0
            1       535a-4eca-8fa0-9cc54c66e11d  2020-01-01  河南   0.0  30.0    0.0
            2       a56d-4415-ad6e-020cdb154c35  2020-01-01  湖北   1.0  30.0   30.0
            3       535a-4eca-8fa0-9cc54c66e11d  2020-01-01  河南   0.0  30.0    0.0
            4       535a-4eca-8fa0-9cc54c66e11d  2020-01-01  河南   0.0  30.0    0.0
            ...                             ...         ...  ..   ...   ...    ...
            100951  8cad-41ee-85b7-c59b85f0ebe6  2020-06-30  湖北  10.0  30.0  300.0
            100952  4ea4-480a-a070-295408955363  2020-06-30  湖北   6.0  30.0  180.0
            100953  70f3-4461-9b5f-7f53a55c51b6  2020-06-30  湖北  10.0  30.0  300.0
            100954  9cc8-4542-8fed-3145e1942504  2020-06-30  湖北  10.0  30.0  300.0
            100955  f202-45df-96e2-ca4e4c389624  2020-06-30  湖北   5.0  30.0  150.0
'''
# print(mask_data.info())
# 查找重复值: duplicated()方法
# print(mask_data.duplicated())
'''
    打印结果为:
        0         False
        1         False
        2         False
        3          True
        4          True
                  ...  
        100951    False
        100952    False
        100953    False
        100954    False
        100955    False
        Length: 100956, dtype: bool
'''
# 查看重复数据
# print(mask_data[mask_data.duplicated()])
# 删除重复数据
mask_data = mask_data.drop_duplicates()
# 查看重复数据
# print(mask_data[mask_data.duplicated()])
# print(mask_data.info())
# 查看 mask_data 的描述性统计信息: describe()方法
# print(mask_data.describe())
'''
    打印结果为:
                        订单量            单价           销售额
            count  1.005080e+05  1.005080e+05  1.005080e+05 # 频数统计: 指对应列有多少有效值
            mean   9.551786e+05  9.552499e+05  9.592048e+05 # 平均值
            std    3.089086e+07  3.089085e+07  3.089073e+07 # 标准差
            min    0.000000e+00  3.000000e+01  0.000000e+00 # 最小值
            25%    9.000000e+00  5.000000e+01  5.500000e+02 # 第一四分位数
            50%    2.000000e+01  5.000000e+01  1.700000e+03 # 中位数
            75%    4.700000e+01  1.500000e+02  4.000000e+03 # 第三四分位数
            max    1.000000e+09  1.000000e+09  1.000000e+09 # 最大值
'''
# 通过布尔索引筛选出单价小于200的数据
mask_data = mask_data[mask_data['单价'] <= 200]
# print(mask_data[mask_data['单价'] <= 200])
# print(mask_data['单价'] <= 200)
# print(mask_data)
# 查看 mask_data 的描述性统计信息: describe()方法
# print(mask_data.describe())
# 筛选订单量大于 0 的数据
mask_data = mask_data[mask_data['订单量'] > 0]
# 查看 mask_data 的描述性统计信息
# print(mask_data.describe())
# 查看以清洗完毕的数据
# print(mask_data)

# 转换日期数据, 并设置对应的日期格式
date_data = pd.to_datetime(mask_data['日期'], format='%Y-%m-%d')
# print(date_data)
# 提取月份信息:
# print(date_data.dt.month)
# mask_data中添加新列
mask_data['月份'] = date_data.dt.month
print(mask_data)

# 将整理后的数据写入csv文件
mask_data.to_csv('./需求数据/mask_data_clear.csv', encoding='gbk', index=False)
