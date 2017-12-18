from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from app import app, mysql
from forms import *
import models

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/search', methods = ['POST', 'GET'])
def search():
	search = request.form['search']
	if request.method == 'POST':
		cur = mysql.connection.cursor()

		cur.execute('SELECT * FROM Student WHERE idNum = %s OR courseId=%s OR firstName=%s OR middleName=%s OR lastName=%s OR sex=%s', (search,search,search,search,search,search,))
		studentSearchs = cur.fetchmany()
		cur.execute('SELECT * FROM Course WHERE courseId = %s OR courseName = %s', (search, search))
		courseSearchs = cur.fetchmany()
		return render_template('search.html', studentSearchs = studentSearchs, courseSearchs = courseSearchs )
	return render_template('home.html')




#STUDENT SECTION
@app.route('/addStudent', methods=['POST', 'GET'])
def addStudent():
	form = AddStudent(request.form)
	if request.method == 'POST' and form.validate():
		idNum = form.idNum.data
		courseId = form.courseId.data
		firstName = form.firstName.data
		middleName = form.middleName.data
		lastName = form.lastName.data
		sex = form.sex.data

		student = models.Student(idNum = idNum, courseId = courseId, firstName = firstName, middleName = middleName, lastName = lastName, sex = sex)
		student.add()
		flash('A student has been successfully added.','success')
	return render_template('addStudent.html', form=form)

@app.route('/listStudent')
def listStudent():
	dis = models.Student.view()
	return render_template("listStudent.html", rows = dis)

@app.route('/updateStudent/<idNum>',methods=['GET','POST'])
def updateStudent(idNum):
	
	cur = mysql.connection.cursor()

	cur.execute("SELECT * FROM Student WHERE idNum = %s", [idNum])

	row = cur.fetchone()

	form = UpdateStudent(request.form)

	if request.method == 'POST' and form.validate():
		courseId = request.form['courseId']
		firstName = request.form['firstName']
		middleName = request.form['middleName']
		lastName = request.form['lastName']
		sex = request.form['sex']

		student = models.Student(idNum = idNum, courseId = courseId, firstName = firstName, middleName = middleName, lastName = lastName, sex = sex)
		student.update()
		cur.close()
		flash('Successfully Updated', 'success')
		return render_template('updateStudent.html', form=form, row=row)
	return render_template('updateStudent.html', form=form, row=row)

@app.route('/deleteStudent/<idNum>')
def deleteStudent(idNum):
	student = models.Student(idNum = idNum, courseId = "", firstName = "", middleName = "", lastName = "", sex = "")
	student.delete()
	flash('Successfully Deleted', 'success')
	return render_template('deleteSuccess.html')

@app.route('/deleteAllStudent')
def deleteAllStudent():
	models.Student.deleteAll()
	flash('All Student has been deleted.', 'success')
	return render_template('deleteSuccess.html')






#COURSE SECTION
@app.route('/addCourse', methods = ['POST', 'GET'])
def addCourse():
	form = AddCourse(request.form)
	if request.method == 'POST' and form.validate():
		courseId = form.courseId.data
		courseName = form.courseName.data

		course = models.Course(courseId = courseId, courseName = courseName)
		course.add()
		flash('A course has been successfully added', 'success')

		return render_template('addCourse.html', form = form)
	return render_template('addCourse.html', form = form)

@app.route('/listCourse')
def listCourse():
	dis = models.Course.view()
	return render_template("listCourse.html", rows = dis)

@app.route('/updateCourse/<courseId>',methods=['GET','POST'])
def updateCourse(courseId):
	
	cur = mysql.connection.cursor()

	cur.execute("SELECT * FROM Course WHERE courseId = %s", [courseId])

	row = cur.fetchone()

	form = UpdateCourse(request.form)

	if request.method == 'POST' and form.validate():
		courseName = request.form['courseName']

		course = models.Course(courseId = courseId, courseName = courseName)
		course.update()
		cur.close()
		flash('Successfully Updated', 'success')
		return render_template('updateCourse.html', form=form, row=row)
	return render_template('updateCourse.html', form=form, row=row)

@app.route('/deleteCourse/<courseId>')
def deleteCourse(courseId):
	cur = mysql.connection.cursor()
	cur.execute('SELECT * FROM Student WHERE courseId = %s', [courseId])
	if cur.fetchone() is not None:
		flash('There are still Students enrolled in this course. Delete the Students first.', 'error')
		return redirect(url_for('listCourse'))
	else:
		course = models.Course(courseId = courseId, courseName = "")
		course.delete()
		flash('Successfully Deleted', 'success')
		return render_template('deleteSuccess.html')
	return redirect(url_for('listCourse'))

@app.route('/deleteAllCourse')
def deleteAllCourse():
	cur = mysql.connection.cursor()
	cur.execute('SELECT * FROM Student')
	if cur.fetchone() is not None:
		flash('There are still Students enrolled. Delete the Students first.', 'error')
		return redirect(url_for('listCourse'))
	else:
		models.Course.deleteAll()
		flash('All Student has been deleted.', 'success')
		return render_template('deleteSuccess.html')
	return redirect(url_for('listCourse'))