import pandas
import sqlalchemy
import pymysql


sqlalchemy_db=sqlalchemy.create_engine("mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata")
sql="select * from t_city_liverent"
read_sql_data=pandas.read_sql(sql=sql,con=sqlalchemy_db)
for i in range(0,3):
    huadong=(read_sql_data['rent'][i]+read_sql_data['rent'][i])/3
print(huadong)
# print(read_sql_data)

