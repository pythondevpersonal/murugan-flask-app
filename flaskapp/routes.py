from flask import render_template, url_for, flash, redirect
from flaskapp import app
from flaskapp.forms import AddForm
from flaskapp.models import Employee

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('create.html', title='Create', form=form)
