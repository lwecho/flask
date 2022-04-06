import json
import flask
from flask import Flask, session
from datetime import timedelta

from flask import request

#创建flask程序
app = Flask(__name__,
            static_url_path='/static',#静态文件路径
            static_folder='static',
            template_folder='templates',#模板文件
            )

#加密字符串
app.config['SECRET_KEY'] = "key123"
#session有效时间
app.config['PERMANENT_SESSION_LIFETIME']= timedelta(days=7)

#字典
@app.route('/abc')
def a_page():

    json_dict ={
        "name":"xiaoli",
        "age":"23",
        "score":"100"
    }
    #字典转化为字符串
    # result = json.dumps(json_dict)

    #json转化为字典
    dict = json.loads('{"age":"22","name":"xiis"}')
    print(dict)
    return 'x'



#设置session
@app.route('/login')
def c_page():

    response = flask.make_response('success')
    flask.session['user_id'] = "20"
    session['vip'] = '0'
    return 'success'

#读取session
@app.route('/d')
def d_page():

    user_id = session['user_id']
    vip = session['vip']
    return flask.render_template('tempa.html',user_id = user_id,vip = vip)

@app.route('/logout')
def logout():
    session.clear()
    return 'logout'




@app.route('/redirect')
def b_page():

    #站外
    #return flask.redirect('http://www.baidu.com')
    #站内
    return flask.redirect(flask.url_for('c_page'))



@app.route('/test')
def test_page():
    #python参数进来都是string类型
    m_int = 100
    m_str = "nihao a"
    m_list = ["xiaoming ","xiaohong","haha"]
    vip = 1
    return flask.render_template("tempa.html",mint=m_int,mstr=m_str,mlist=m_list,vip=vip)



#404重定向
@app.errorhandler(404)
def page_not_found(e):
    return '你出错了',404


#过滤器
@app.template_filter('dore')
def do_reverse(li):
    temp = list(li)
    temp.reverse()
    return temp



@app.route('/')
def index():
    return "haha"
    pass


if __name__ == '__main__':

    app.run(port=8888,debug=True)