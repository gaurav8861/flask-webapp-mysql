from flask import Flask, render_template, request
import pymysql
app = Flask(__name__)
class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "root"
        db = "test"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
    def list_employees(self):
        self.cur.execute("SELECT firstName, lastName FROM MyUsers LIMIT 50")
        result = self.cur.fetchall()
        return result
@app.route('/')
def employees():
    def db_query():
        db = Database()
        emps = db.list_employees()
        return emps
    res = db_query()
    return render_template('index.html', result=res, content_type='application/json')

@app.route('/add', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        db = Database()
        db.cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        db.cur.connection.commit()
        db.cur.close()
        return 'success'
    return render_template('form-emp.html')
