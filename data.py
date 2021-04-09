from flask import Flask, render_template
import sqlalchemy
import pandas as pd
import numpy as np
import pymysql
import json

# 创建服务
app = Flask(__name__)

# 访问根目录时，默认返回templates里的html文件
@app.route('/bar', methods=['GET', 'POST'])
def bar():
    return render_template('bar.html')

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    return  render_template('pie.html')



# 前端ajax请求，获取数据的路由
@app.route('/bardata', methods=['GET', 'POST'])
def bar_data():
    return  get_bar_data()

@app.route('/piedata', methods=['GET', 'POST'])
def pie_data():
    return  get_pie_data()


# 定义方法获取数据
def get_bar_data():
    # 从数据库里获取数据
    engine = sqlalchemy.create_engine('mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata')
    data_frame = pd.read_sql_table(table_name='bar', con=engine)

    xvalues = data_frame['name'].values
    yvalues = data_frame['price'].values


    json_data = {
        'xvalue': xvalues.tolist(),
        'yvalue1': yvalues.tolist(),
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



if __name__ == '__main__':
    app.run(debug=True, port='5000')