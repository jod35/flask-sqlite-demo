from flask import Flask,render_template,request,flash,redirect,session
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

            if bcrypt.check_password_hash(user_password[0][0],password):

                session['logged_in']=True
                
                return redirect('/loggedin')
            else:
                flash("The account doesnot exist")
                return redirect('/login')
    return render_template('login.html')
    
@app.route('/loggedin')
def logged_in():
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        return render_template('logged_in.html')

@app.route('/logout')
def logout():
    session['logged_in']=False
    return redirect('/login')
