"""
CSV:CSV 文件又称为逗号分隔值文件，是一种通用的、相对简单的文件格式，用以存储表格数据，包括数字或者字符。
    CSV 是电子表格和数据库中最常见的输入、输出文件格式
CSV模块:
    csv.reader	    返回一个遍历 CSV 文件各行的读取器对象
    csv.writer	    返回将数据写入 CSV 文件的写入器对象
    csv.register_dialect	注册 CSV 方言
    csv.unregister_dialect	注销 CSV 方言
    csv.get_dialect	返回具有给定名称的方言
    csv.list_dialects	返回所有已注册的方言
    csv.field_size_limit	返回解析器允许的当前最大字段大小
"""
import csv
"""
csv.writer()
    格式:writer(csvfile, dialect='excel', **fmtparams)
    dialect：编码风格，默认为 excel 的风格，也就是使用逗号,分隔。
    fmtparam：格式化参数，用来覆盖之前 dialect 对象指定的编码风格。
"""
# 操作文件对象时,需要添加newline逐行写入，否则会出现空行现象
with open('egg.csv','w',newline='') as csv_f:
    # delimiter 指定分隔符，默认为逗号，这里指定为空格
    # quotechar 表示引用符
    # writerow 单行写入，列表格式传入数据
    spamwriter = csv.writer(csv_f, delimiter=' ')
    spamwriter.writerow('hello,world')
    spamwriter.writerow('my name is jamin')
    spamwriter.writerow('who are you?')

"""
DictWriter()
    格式:DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds
    创建一个对象，该对象在操作上类似常规 writer，但会将字典映射到输出行。 
    fieldnames 参数是由键组成的 序列，它指定字典中值的顺序，这些值会按指定顺序传递给 writerow() 方法并写入文件 f。 
    如果字典缺少 fieldnames 中的键，则可选参数 restval 用于指定要写入的值。 
    如果传递给 writerow() 方法的字典的某些键在 fieldnames 中找不到，则可选参数 extrasaction 用于指定要执行的操作。 
    如果将其设置为默认值 'raise'，则会引发 ValueError。 
    如果将其设置为 'ignore'，则字典中的其他键值将被忽略。 所有其他可选或关键字参数都传递给底层的 writer 实例。
"""
with open('dict.csv', 'w', newline='') as csvfile:
    # 创建要写入的key值，也就是字典的键
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})