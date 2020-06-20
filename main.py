from flask import Flask,render_template,request,flash,redirect
from flask_bcrypt import Bcrypt


from .models import insert_record


app=Flask(__name__)

app.secret_key='youarenotthatmuchsecretsobetterwatchout'
bcrypt=Bcrypt(app)


@app.route('/',methods=['GET','POST'])
def sign_up_form():
    if request.method == 'POST':

        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        confirm=request.form['confirm']

        if password == confirm:
            pass
        else:
            flash("Passwords do not match!!")
            return redirect('/')

        pwd_hash=bcrypt.generate_password_hash(password)
        insert_record(name,email,pwd_hash)
        flash("Records added successfully")
    return render_template('index.html')


@app.route('/')
def login():
    