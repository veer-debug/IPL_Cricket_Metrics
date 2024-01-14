from flask import Flask,render_template,redirect,request,session
import requests
from mydb import Database
# import api


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




@app.route('/tvt')
def home():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()['teams']
    return render_template('teamvsteam.html',teams = sorted(teams))

@app.route('/teamvteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = requests.get('http://127.0.0.1:5000/api/teamvteam?team1={}&team2={}'.format(team1,team2))
    response = response.json()

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json()['teams']

    return render_template('teamvsteam.html',result = response,teams = sorted(teams))



@app.route('/team')
def team_vs_team():
    return render_template('teaam.html')
@app.route('/batsman')
def team_vs_team():
    return render_template('basmen.html')
    
@app.route('/bolwer')
def team_vs_team():
    return render_template('boller.html')

app.run(debug=True,port=7500)



