"""
条件语句:
    if.....elif.....else.....
结构 :
    1.if...elif(多个)
    2.if...elif(多个)...else
    3.if...else...
含义 :
    1.if - 满足输出的条件
    2.elif - 当不满足if的输出的条件，便输出elif的条件(多个elif就有多个条件)，直到没有elif语句
    3.else - 不满足其以上的所有条件输出
"""

# 用户身份验证
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
username = input('请输入用户名: ')
password = input('请输入口令: ')

if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')


# 成绩等级
score= int(input('请输入成绩:'))
if score >= 80 :
    print('A')
elif score >= 70:
    print('B')
elif score >= 80:
    print('C')
else:
    print('D')


# 输术
country = input('请选择法国/葡萄牙/阿根廷/巴西中的一个输入:')
if country == '巴西':
    print('内马尔')
elif country == '葡萄牙':
    print(c罗)
elif country == 'agt':
    print('梅西')
elif country == '法国':
    print('姆巴佩')
else:
    print('查无此人')

"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))

"""分支结构的嵌套"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))