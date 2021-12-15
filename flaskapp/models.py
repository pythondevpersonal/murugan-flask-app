from datetime import datetime
from flaskapp import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(20), unique=True, nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    employees = db.relationship('Employee', backref='company', lazy=True)

    def __repr__(self):
        return f"User('{self.company_name}')"

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    date_employed = db.Column(db.DateTime, default=datetime)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    salary = db.Column(db.Integer, default=0)
    address = db.Column(db.Text, nullable=True)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"