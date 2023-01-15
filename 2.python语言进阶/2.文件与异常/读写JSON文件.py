"""
json:轻量级的数据交换格式
例子:
    {
    "name": "骆昊",
    "age": 38,
    "qq": 957658,
    "friends": ["王大锤", "白元芳"],
    "cars": [
        {"brand": "BYD", "max_speed": 180},
        {"brand": "Audi", "max_speed": 280},
        {"brand": "Benz", "max_speed": 320}
    ]
}
可能大家已经注意到了，上面的JSON跟Python中的字典其实是一样一样的，事实上JSON的数据类型和Python的数据类型是很容易找到对应关系的，
如下面两张表所示：
    JSON	Python
    object	dict
    array	list
    string	str
    number (int / real)	int / float
true / false	True / False
    null	None

    Python	  JSON
    dict	 object
    list,  tuple	array
    str	     string
    int,  float, int- & float-derived Enums	number
 True/False	 true / false
    None	 null
"""
import json


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()

"""
json模块主要有四个比较重要的函数，分别是：
    dump - 将Python对象按照JSON格式序列化到文件中
    dumps - 将Python对象处理成JSON格式的字符串
    load - 将文件中的JSON数据反序列化成对象
    loads - 将字符串的内容反序列化成Python对象
"""