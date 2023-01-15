"""创建mysql的数据库链接"""
from pymysql import Connection
con = Connection(
    host = 'localhost', # 服务器地址(ip地址)
    port = 3306,    # 端口
    user = 'root',  # 用户名
    password = '20020621',# 密码
    # autocommit= True  #默认确认，不用指令提交
)
执行非查询性质sql
print(con.get_server_info())

获取游标对象
cur = con.cursor()
选择数据库
con.select_db('world')
执行sql
cur.execute('create table test_mysql(id int);')
cur.execute('select * from student;')
获取查询结果
results = cur.fetchall()
for i in results:
    print(i)
关闭链接
con.close()

"""数据插入"""
cur = con.cursor()
con.select_db("world")
cur.execute("insert into student values(6,'姆巴佩',31,'职业球员','男')")
#确认操作-改变数据都需要commit()
con.commit()
con.close()

