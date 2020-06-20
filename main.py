from flask import Flask,render_template,request,flash,redirect
from flask_bcrypt import Bcrypt
from .models import insert_record,retrieve_user_password


app=Flask(__name__)

app.secret_key='youarenotthatmuchsecretsobetterwatchout'
bcrypt=Bcrypt(app)


@app.route('/',methods=['GET','POST'])
def sign_up_form():
    if request.method == 'POST':

        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        confirm=request.form.get('confirm')

        if password == confirm:
            pass
        else:
            flash("Passwords do not match!!")
            return redirect('/')

        pwd_hash=bcrypt.generate_password_hash(password)
        insert_record(name,email,pwd_hash)
        flash("Records added successfully")
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():

    if request.method =='POST':
        email=request.form.get('email')
        password=request.form.get('password')

        if retrieve_user_password(email):
            user_password=retrieve_user_password(email)
            print(bcrypt.check_password_hash(user_password[0][0],password))
    return render_template('login.html')
    