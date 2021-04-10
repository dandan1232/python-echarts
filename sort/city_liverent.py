import pandas
import sqlalchemy
import pymysql

sqlalchemy_db=sqlalchemy.create_engine("mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata")
sql="select*from t_city_liverent order by rent desc"
read_sql_data=pandas.read_sql(sql=sql,con=sqlalchemy_db)
for i in range(0, read_sql_data.__len__()):
    # print(read_sql_data)
    # print(i)
    print("=="+str(i+1)+"."+str(read_sql_data['city'][i])+"省=住宿场所个数为"+str(read_sql_data['num'][i])+
          "个=出租率为:"+str((read_sql_data['rent'][i])*100)+"%===")
    print('%.2f'%read_sql_data['rent'][i])