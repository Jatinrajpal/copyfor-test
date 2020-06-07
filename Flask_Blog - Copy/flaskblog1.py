from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, EmployeeForm, AdminForm, otpForm
from os import listdir
from bson import ObjectId
from flask_pymongo import MongoClient
import math
import urllib.request
import urllib.parse
import random
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
 
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # print (resp)
        flash(f'added','success')
        return redirect(url_for('details'))
    return render_template('register.html', title='SignUp', form=form)

@app.route("/details",methods=['GET', 'POST'])
def details():
    form = AdminForm()
    if request.method=='POST' and form.validate():
        phno=form.mobileno.data
        flash(f'added to ATeva','success')
        return redirect(url_for('otp'))
    return render_template('details.html',title='Details',form=form)

@app.route("/otp",methods=['GET', 'POST'])
def otp():
    form=otpForm()
    otp=random.randint(100000,999999)
    resp =  sendSMS('PJWli8WnceU-tWPszSeAWo6sIHpFYvuGO2pHY2NKqh', '9079932715','TXTLCL', 'Your Verification code is '+str(otp))
    if request.method=='POST' and form.validate():
        flash(f'enter otp','success')
        if form.otp.data==otp:
            flash(f'added','success')
        else:
            flash(f'error','success')
    return render_template('otp.html',title='OTP',form=form)

@app.route("/registeruser",methods=['GET','POST'])
def registeruser():
    form=EmployeeForm()
    if request.method=='POST' and form.validate():
        flash(f'welcome to the company user','success')
    return render_template('registeruser.html',title='Add',form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('registeruser'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
