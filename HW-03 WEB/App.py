from crypt import methods
from flask import Flask, Request, Response, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
app = Flask(__name__, template_folder='template')
app.secret_key="CRUDflaskapp"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class susmitha(db.Model):
    __tablename__ = 'student'
    _id = db.Column('id',db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(100))
    marks = db.Column(db.Integer)

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
@app.before_first_request
def create_tables():
    db.create_all()
@app.route('/')
def susmithah():
    return render_template('susmithah.html')
@app.route('/add_record',methods=['GET', 'POST'])
def add_record():
    if request.method == "POST":
       first_name = request.form.get("fname")
       last_name = int(request.form.get("lname"))
       record = susmitha(first_name,last_name)
       db.session.add(record)
       db.session.commit()
       return render_template("susmithah.html", msg = "Data added successfully")
    else:
        return Response('Cannot add the given data')

@app.route('/get_records',methods=['GET', 'POST'])
def get_records():
    if request.method == "POST":
        check = request.form.get("type")
        regular_data = susmitha.query.order_by(susmitha._id).all()
        pass_data = susmitha.query.filter(susmitha.marks>=85).all()
        if check=="True":
            return render_template("susmithah.html", data = pass_data)
        else:
            return render_template("susmithah.html", data = regular_data)
        
    else:
        return Response("Not responding")

@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    if request.method == "POST":
        id = request.form.get("id")
        susmitha.query.filter(susmitha._id == id).delete()
        db.session.commit()
        return render_template("susmithah.html", delmsg = "Student Deleted")

app.run(debug=True)