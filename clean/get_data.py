import sqlalchemy
import pandas as pd
import numpy as np
import pymysql
import json


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
    engine =sqlalchemy.create_engine('mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata')
    data_frame =pd.read_sql_table(table_name='t_city_liverent',con=engine)
    xvalues =data_frame['city'].values
    yvalues =data_frame['rent'].values

    json_data={
        'xvalue':xvalues.tolist(),
        'yvalue':yvalues.tolist(),
    }

    json_string =json.dumps(json_data,ensure_ascii=False)
    return json_string