import pandas
import sqlalchemy
import pymysql


sqlalchemy_db=sqlalchemy.create_engine("mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata")
sql="select * from t_city_liverent"
read_sql_data=pandas.read_sql(sql=sql,con=sqlalchemy_db)
print(read_sql_data)
data = read_sql_data.sort_values(by='rent',axis=0, ascending=False)
data.reset_index(drop=True, inplace=True)

if __name__ == '__main__':
    print(data)
for i in range(0, data.__len__()):
    # print(read_sql_data)
    # print(i)
    print("=="+str(i+1)+"."+str(data['city'][i])+"省=住宿场所个数为"+str(data['num'][i])+
          "个=出租率为:"+str('%.2f'%((data['rent'][i])*100))+"%===")
    # print('%.2f'%read_sql_data['rent'][i])