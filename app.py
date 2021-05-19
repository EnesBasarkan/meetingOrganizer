from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.secret_key = "Secret Key"
 
#SqlAlchemy Database Configuration With SQLITE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
#Creating meets table for our CRUD database
class Data(db.Model):
    __tablename__ = "meets"
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    subject = db.Column(db.String,nullable=False)
    date = db.Column(db.String,nullable=False)
    start_time = db.Column(db.String,nullable=False)
    end_time = db.Column(db.String,nullable=False)
    participants = db.Column(db.String,nullable=False)
 
    def __init__(self, subject, date, start_time,end_time,participants):
 
        self.subject =subject
        self.date = date
        self.start_time =start_time
        self.end_time =end_time
        self.participants =participants
 
@app.route('/')
def Index():
    all_data = Data.query.all()
    return render_template("index.html", meets = all_data)


#This route is for inserting data 
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        subject =request.form['subject']
        date = request.form['date']
        start_time =request.form['start_time']
        end_time =request.form['end_time']
        participants =request.form['participants']
 
        my_data = Data(subject, date, start_time,end_time,participants)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Meet Inserted Successfully")
 
        return redirect(url_for('Index'))
 