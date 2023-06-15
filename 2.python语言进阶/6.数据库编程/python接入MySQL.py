import pymysql
# 创建 MySQL 连接
con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='20020621',
    charset='utf8mb4'
)

# 获取游标对象
cur = con.cursor()

# 使用数据库
cur.execute('use world')

# 执行 SQL 查询语句
cur.execute('select * from student')

# 获取查询结果
results = cur.fetchall()
print(results)

# 关闭游标和数据库连接
cur.close()
con.close()

"""数据插入"""
# 插入数据
# cur.execute("insert into student (id, name, age, occupation, gender) values (6, '姆巴佩', 31, '职业球员', '男')")

# 确认提交操作
# con.commit()

# 关闭游标和数据库连接
# cur.close()
# con.close()


