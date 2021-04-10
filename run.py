from flask import Flask, render_template
from clean import  get_data

# 创建服务
app = Flask(__name__)

# 访问根目录时，默认返回templates里的html文件
@app.route('/bar', methods=['GET', 'POST'])
def bar():
    return render_template('bar.html')

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    return  render_template('pie.html')

@app.route('/city_liverent_bar',methods=['GET','POST'])
def city_liverent_bar():
    return render_template('city_liverent_bar.html')



# 前端ajax请求，获取数据的路由
@app.route('/bardata', methods=['GET', 'POST'])
def bar_data():
    return  get_data.get_bar_data()

@app.route('/piedata', methods=['GET', 'POST'])
def pie_data():
    return  get_data.get_pie_data()

@app.route('/city_liverent_bardata',methods=['GET','POST'])
def city_liverent_bar_data():
    return get_data.get_city_liverent_bar_data()


if __name__ == '__main__':
    app.run(debug=True, port='5000')