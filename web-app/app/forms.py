from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField, validators, ValidationError
from flask_mysqldb import MySQL
from app import app, mysql

def courseIdStudentChecker(form, field):
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM Course WHERE courseId = %s", [field.data])
	course = cur.fetchone()
	if course is None:
		raise ValidationError('The course ID is not found.')

def idNumChecker(form, field):
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM Student WHERE idNum = %s", [field.data])
	student = cur.fetchone()
	if student is not None:
		raise ValidationError('The ID Number is already taken.')

def courseIdCourseChecker(form, field):
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM Course WHERE courseId = %s", [field.data])
	course = cur.fetchone()
	if course is not None:
		raise ValidationError('The Course ID is already taken.')


class AddStudent(Form):
	idNum = StringField('ID Number:', [validators.Length(min = 1, message = 'This Data is Required.'), idNumChecker])
	courseId = StringField('Course ID:', [validators.Length(min = 1, message = 'This Data is Required.'), courseIdStudentChecker])
	firstName = StringField('First Name:', [validators.Length(min=1, message = 'This Data is Required.')])
	middleName = StringField('Middle Name:', [validators.Length(min=1, message = 'This Data is Required.')])
	lastName = StringField('Last Name:', [validators.Length(min=1, message = 'This Data is Required.')])
	sex = StringField('Sex:', [validators.Length(min=1, message = 'This Data is Required.'), validators.AnyOf(values = ['M','m','F','f'], message = 'Answer only M or F.')])

class AddCourse(Form):
	courseId = StringField('Course ID:', [validators.Length(min = 1, message = 'This Data is Required.'), courseIdCourseChecker])
	courseName = StringField('Course Name:', [validators.Length(min = 1, message = 'This Data is Required.')])

class UpdateStudent(Form):
	courseId = StringField('Course ID:', [validators.Length(min = 1, message = 'This Data is Required.'), courseIdStudentChecker])
	firstName = StringField('First Name:', [validators.Length(min=1, message = 'This Data is Required.')])
	middleName = StringField('Middle Name:', [validators.Length(min=1, message = 'This Data is Required.')])
	lastName = StringField('Last Name:', [validators.Length(min=1, message = 'This Data is Required.')])
	sex = StringField('Sex:', [validators.Length(min=1, message = 'This Data is Required.'), validators.AnyOf(values = ['M','m','F','f'], message = 'Answer only M or F.')])

class UpdateCourse(Form):
	courseName = StringField('Course Name:', [validators.Length(min = 1, message = 'This Data is Required')])