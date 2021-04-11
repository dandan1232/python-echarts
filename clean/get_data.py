import pandas
import sqlalchemy
import pandas as pd
import numpy as np
import pymysql
import json

from sort.city_liverent import sqlalchemy_db


def get_bar_data():
    # 从数据库里获取数据
    engine = sqlalchemy.create_engine('mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata')
    data_frame = pd.read_sql_table(table_name='bar', con=engine)

    xvalues = data_frame['name'].values
    yvalues = data_frame['price'].values

    json_data = {
        'xvalue': xvalues.tolist(),
        'yvalue': yvalues.tolist(),
    }

    json_string = json.dumps(json_data, ensure_ascii=False)
    return json_string


def get_pie_data():
    engine = sqlalchemy.create_engine('mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata')
    data_frame = pd.read_sql_table(table_name='pie', con=engine)
    names = data_frame['name'].values
    values = data_frame['value'].values
    json_array = []
    for i in range(0, names.__len__()):
        json_array.append({'name': names[i], 'value': values[i]})
    json_data_array = {
        'data_pie': json_array
    }

    json_string = json.dumps(json_data_array, ensure_ascii=False)
    return json_string


def get_city_liverent_bar_data():
    engine = sqlalchemy.create_engine('mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata')
    sql = "select * from t_city_liverent order by rent desc"
    # data_frame =pd.read_sql(table_name='t_city_liverent',con=engine)
    data_frame = pandas.read_sql(sql=sql, con=engine)

    xvalues = data_frame['city'].values
    yvalues = data_frame['rent'].values
    new_y = []
    for i in range(0, yvalues.__len__()):
        new_y.append(int(yvalues[i] * 100))

    json_data = {
        'xvalue': xvalues.tolist(),
        'yvalue': new_y,
    }
    # print(json_data['yvalue'])

    json_string = json.dumps(json_data, ensure_ascii=False)
    return json_string


def stacked_line_data():
    engine = sqlalchemy.create_engine('mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata')
    sql = "select * from stacked_line"
    print(sql)
    data_frame = pandas.read_sql(sql=sql, con=engine)

    yi = data_frame['yi'].values
    er = data_frame['er'].values
    san = data_frame['san'].values
    si = data_frame['si'].values
    wu = data_frame['wu'].values

    json_data = {
        'yi': yi.tolist(),
        'er': er.tolist(),
        'san': san.tolist(),
        'si': si.tolist(),
        'wu': wu.tolist(),
    }
    json_string = json.dumps(json_data, ensure_ascii=False)
    return json_string


def bar_line_data():
    engine = sqlalchemy.create_engine('mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata')
    sql = "select * from book"
    # print(sql)
    data_frame = pandas.read_sql(sql=sql, con=engine)
    # print(data_frame)
    xvalues = data_frame['name'].values
    yvalues = data_frame['price'].values

    for i in range(0, yvalues.__len__()):
        yvalues[i] = float(yvalues[i][0: yvalues[i].__len__() - 2])
    # print(clean_yvalues)

    json_data = {
        'xvalue': xvalues.tolist(),
        'yvalue': yvalues.tolist(),
    }
    json_string = json.dumps(json_data, ensure_ascii=False)
    return json_string
