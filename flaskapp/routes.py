from flask import render_template, url_for, flash, redirect,request
from flaskapp import app,db
from flaskapp.forms import AddForm
from flaskapp.models import Company, Employee

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
def add():
    form = AddForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('/'))
    companies = Company.query.order_by(Company.date_created).all()
    return render_template('create.html', title='Create', form=form,companies=companies)
