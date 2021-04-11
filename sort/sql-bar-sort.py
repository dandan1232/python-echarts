import pymysql
import sqlalchemy
import pandas


# 使用pymysql连接数据库
# pymysql_db =pymysql.connect(host="localhost",user="root",password="ldd123789dd",db="bigdata",port=3306,charset="utf8")

# sql查询语句，查询数据表中的前五条信息
sql= "select*from bar order by id desc limit 4"

# 通过read_sql_query()函数读取数据库信息
# sql_query_data =pandas.read_sql(sql=sql,con=pymysql_db)

# 使用sqlalchemy连接数据库，依次设置（数据库产品名称+数据库操作模块名://数据库用户名：密码@数据库ip地址：数据库端口号/数据库名称）
sqlalchemy_db=sqlalchemy.create_engine("mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata")


# 通过read_sql()函数读取数据库信息
read_sql_data=pandas.read_sql(sql=sql,con=sqlalchemy_db)

# series=pandas.Series(read_sql_data.values)


    # print("通过read_sql_query()函数读取数据库信息如下：\n",sql_query_data)
if __name__ == '__main__':
    print("通过read_sql()函数读取数据库信息如下：\n",read_sql_data)
    print(read_sql_data['price'][0])
for i in range(0,4):
    print('id为',read_sql_data['id'][i],'name为',read_sql_data['name'][i])
