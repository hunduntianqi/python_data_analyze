"""
    pandas库:
        是一个专门用来解决数据分析问题的库
        两大优势:
            1. 速度快: 快速处理大型数据集
            2. 效率高: 提供大量高效处理数据的函数和方法
        给库起别名的方法:
            import 要导入的库 as 库的别名
        导入pandas库并简化库名:
            import pandas as pd
        pandas库的基本数据结构:
            1. Series:
                主要由一组数据及其对应的索引组成, Series对象左侧为对应索引, 右侧为索引对应数据
            2. DataFrame:
                是一种表格型的数据结构, 包含行索引, 列索引以及一组数据
        Series对象和DataFrame对象的联系:
            >> DataFrame 对象可以被看作是由Series对象所组成的!!
            可以通过DataFrame[列索引]取出DataFrame对象中的一列数据
        读取csv文件:
            pd.read_csv(filepath_or_buffer, sep, encoding, engine):
                filepath_or_buffer: 要读取文件的路径, 可以是绝对路径, 也可以是相对路径, 参数类型为字符串
                sep: 指定分割符, 否则读取数据不分列
                encoding: 要读取文件的编码格式, 参数类型为字符串
                engine: 指定为'python'即可, 否则会报错
                该方法返回一个DataFrame对象
        DatFrame.info()方法:
            可以帮助我们提炼出DataFrame对象的基本数据信息, 其中包括:整体数据的总行数、
            各列数据类型统计、各列的列名、各列总共有多少非空数据、表格占用的系统空间等
        isna()方法:
            在pandas库中, 可以使用isna()方法来查找DataFrame对象和Series对象中的缺失值,
            该方法将查找结果以 DataFrame 对象或者 Series 对象的形式进行返回, 返回对象中
            的内容都是布尔值, 缺失数据会用 True 来表示, False 则代表这里的数据不缺失
        DataFrame.head()方法: 默认可以查看数据的前 5 行
        DataFrame.tail()方法: 默认可以查看数据的后 5 行
        dropna()方法:
            使用dropna()方法可以直接删除DataFrame对象和Series对象中的缺失值数据
            注意: 该方法不会改变原来DataFrame对象的值, 会返回一个新的DataFrame对象
            指定列索引删除缺失值:
                DataFrame.dropna(subset=[列索引1, 列索引2, ...])
"""