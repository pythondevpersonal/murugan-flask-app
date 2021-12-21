from flask import render_template, url_for, flash, redirect,request
from flaskapp import app,db
from flaskapp.forms import AddForm
from flaskapp.models import Company, Employee
from datetime import datetime

@app.route('/company', methods=['POST','GET'])
def company():
    if request.method== 'POST':
        company_name = request.form['company_name']
        new_company = Company(company_name=company_name)

        try:
            db.session.add(new_company)
            db.session.commit()
            flash(f'Company created for {company_name}!', 'success')
            return redirect('/company')

        except:
            return 'There was a issue'

    else:
        companies = Company.query.order_by(Company.date_created).all()
        return render_template('company.html',companies=companies)

@app.route("/", methods=['GET', 'POST'])
def index():
    employees = Employee.query.order_by(Employee.username).all()
    return render_template('index.html',employees=employees)

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        splitted_text= request.form['dob'].split('-')
        dob = datetime(int(splitted_text[0]), int(splitted_text[1]), int(splitted_text[2]))
        date_employed = datetime(2012, 3, 3, 10, 10, 10)
        image_file = 'test'   
        company_id = request.form['company_id']
        
        salary = 100
        address = 'test address'
        new_employee = Employee(username=username,name=name,email=email,phone=phone,dob=dob,date_employed=date_employed,image_file=image_file,company_id=company_id,salary=salary,address=address)
        
        try:
            db.session.add(new_employee)
            db.session.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect('/')
        
        except:
            return 'There is an issue'

       
    companies = Company.query.order_by(Company.date_created).all()
    return render_template('create.html', title='Create', form=form,companies=companies)

@app.route('/employee/update/<int:id>', methods=['GET','POST'])
def update(id):
    form = AddForm()
    if request.method == 'POST' and form.validate_on_submit():
        employee = Employee.query.get_or_404(id)
        employee.username = request.form['username']
        employee.name = request.form['name']
        employee.email = request.form['email']
        employee.phone = request.form['phone']
        splitted_text= request.form['dob'].split('-')
        employee.dob = datetime(int(splitted_text[0]), int(splitted_text[1]), int(splitted_text[2]))
        employee.date_employed = datetime(2012, 3, 3, 10, 10, 10)
        image_file = 'test'   
        employee.company_id = request.form['company_id']

        try:
             db.session.commit()
             flash(f'Account updated for {form.username.data}!', 'success')
             return redirect('/')
        except:
            return 'There is an error'

    else:
        employee_to_view = Employee.query.get_or_404(id)
        companies = Company.query.order_by(Company.date_created).all()
        return render_template('view_employee.html',employee=employee_to_view,form=form,companies=companies)


@app.route('/employee/delete/<int:id>', methods=['GET'])
def delete(id):
    employee_to_delete = Employee.query.get_or_404(id)

    try:
        db.session.delete(employee_to_delete)
        db.session.commit()
        flash(f'Account deleted for {employee_to_delete.username}!', 'success')
        return redirect('/')
    except:
        return "error in deletion"