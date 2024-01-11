from flask import Flask,render_template,redirect,request,session
from mydb import Database
import api


app=Flask(__name__)

dbo=Database()

@app.route('/')

def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_egistration',methods=['post'])
def perform_registration():
    name=request.form.get('username')
    email=request.form.get('email')
    password=request.form.get('password')
    con_password=request.form.get('confirm-password')
    if password ==con_password:
        respons=dbo.insert(name,email,password)
        if respons:
            return render_template('login.html',message="Regestration Successful. Kindly login to proceed")
        else:
            return render_template('register.html',message="Email alredy exist")
    else:
        return render_template('register.html',message="Password not match")

@app.route('/perform_login',methods=['post'])
def perform_login():
    email=request.form.get('email')
    password=request.form.get('password')
    respons=dbo.search(email,password)
    if respons:
        return redirect('/profile')
    else:
        return render_template('login.html',message="User not defined")


@app.route('/profile')
def profile():
    
    return render_template('profile.html')



    

        
app.run(debug=True)


