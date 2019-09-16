import pymysql
from flask import Flask, render_template, request
from numpy.distutils.fcompiler import none

app = Flask(__name__)
from flaskext.mysql import MySQL
from tabulate import tabulate
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'tejas'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'clippy_users'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
table = {}
q = ''


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ID = request.form['ID']
        view(ID)
    return render_template('home.html', table=table)


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        id = request.form['ID']
        username = request.form['username']
        password = request.form['password']
        print(id, username, password)
        data = insert_table(id, username, password)
    return render_template('insert.html')  # , table=table)


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        id = request.form['ID']
        username = request.form['username']
        password = request.form['password']
        print(id, username, password)
        data = update_table(id, username, password)
    return render_template('update.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        ID = request.form['ID']
        print(ID)
        delete_table(ID)
    return render_template('delete.html', q=q)


def view(ID):
    global table
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clippy_admin_users where ID=" + ID)
    data = cursor.fetchone()
    # table = tabulate(data, headers=['ID', 'Name', 'Password'], tablefmt='orgtbl')
    table = data
    return table


def insert_table(ID, username, password):
    try:
        connection = mysql.connect()
        cursor = connection.cursor()
        sql = "insert into clippy_admin_users values({0},'{1}','{2}');".format(ID, username, password)

        print(sql)
        cursor.execute(sql)
        connection.commit()
        print(cursor.rowcount, "record inserted.")
    except:
        import sys
        print(sys.exc_info())
    return table


def update_table(ID, username=none, password=none):
    try:
        if username == '' and password == '':
            connection = mysql.connect()
            cursor = connection.cursor()
            sql = "select * from clippy_admin_users where id=" + ID
            data = cursor.fetchone()
        elif username != '' or password != '':
            connection = mysql.connect()
            cursor = connection.cursor()
            sql = "update clippy_admin_users set username='{0}', password='{1}' where id={2}".format(username, password,
                                                                                                     ID)
            print(sql)
            cursor.execute(sql)
            connection.commit()
            print(cursor.rowcount, "record updated.")
    except:
        import sys
        print(sys.exc_info())
    return table


def delete_table(ID):
    try:
        connection = mysql.connect()
        cursor = connection.cursor()
        sql = "delete from clippy_admin_users where id=" + ID
        cursor.execute(sql)
        connection.commit()
        q = 'user deleted'
    except:
        import sys
        print(sys.exc_info())
    return table


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
