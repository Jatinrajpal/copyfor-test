from flask_wtf import FlaskForm
from wtforms.fields import html5 as h5fields
from wtforms import StringField,PasswordField,SubmitField,BooleanField,IntegerField,validators
from wtforms.validators import DataRequired,Length,Email,EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired

class AdminForm(FlaskForm):
		name=StringField('Name',[validators.Length(min=4, max=25)])
		orgname=StringField('OragnizationName',[validators.Length(min=5,max=25)])
		mobileno=StringField('Phone Number',[validators.Length(min=10,max=10)])
		getotp=SubmitField('GetOTP')
		
class otpForm(FlaskForm):
		otp=StringField('OTP',[validators.Length(min=6,max=6)])
		submit=SubmitField('VERIFY')

class EmployeeForm(FlaskForm):
		employeename=StringField('EmployeeName',[validators.Length(min=6,max=25)]);
		employeeid=StringField('Employee id',validators=[DataRequired()])
		mobileno=StringField('Phone No',[validators.Length(min=10,max=10)])
		department=StringField('Department',validators=[DataRequired()])
		profilephoto=FileField('Profile Photo', validators=[FileRequired(),FileAllowed(['jpg','png'], 'Images only!')])
		submit=SubmitField('Add')

class RegistrationForm(FlaskForm):
		productkey=StringField('ProductKey',validators=[DataRequired()])
		username=StringField('Username',validators=[DataRequired()])
		password = PasswordField('Password', validators=[DataRequired()])
		confirmpassword = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
		submit=SubmitField('SignUp')

class LoginForm(FlaskForm):
		username=StringField('Username',validators=[DataRequired()])
		password=PasswordField('Password',validators=[DataRequired()])
		submit=SubmitField('Login')