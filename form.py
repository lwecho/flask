from flask import *

import pymysql

app = Flask(__name__,
            static_url_path='/static',#静态文件路径
            static_folder='static',
            template_folder='templates',#模板文件
            )


@app.route('/chuli',methods=['POST'])
def chuli():
    if request.method=="POST":
        username = request.form.get("uname")
        password = request.form.get("passwd")
        print("用户名："+username+"密码"+password)

    #打开数据库
    db = pymysql.connect(host="localhost",user="root",password="759520",db="test")
    #创建游标对象
    cursor = db.cursor()

    sql = """
    select * from admin
    """

    #执行sql
    cursor.execute(sql)

    db.commit()

    list1 = []
    for temp in cursor.fetchall():
        dict = {'name':temp[0],'pass':temp[1]}
        list1.append(dict)
    print(list1)

    db.close()

    return render_template('chuli.html',list1 = list1)


@app.route('/test1')
def test1():
    return render_template('test1.html')




@app.route('/')
def index():
    return "hh"

@app.errorhandler(404)
def page_not_found(e):
    return '你出错了',404

if __name__ == '__main__':
    app.run(debug=True)