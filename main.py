from flask import Flask,render_template,request,flash

from .models import insert_record


app=Flask(__name__)



@app.route('/',methods=['GET','POST'])
def sign_up_form():
    if request.method == 'POST':

        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        confirm=request.form['confirm']

        insert_record(name,email,password)

        return "record added successfully"






    return render_template('index.html')