from app import mysql



class Student:

	def __init__(self, idNum, courseId, firstName, middleName, lastName, sex):
		self.idNum = idNum
		self.courseId = courseId
		self.firstName = firstName
		self.middleName = middleName
		self.lastName = lastName
		self.sex = sex

	@staticmethod
	def view():
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM Student")
		dis = cur.fetchall()
		return dis

	
	def add(self):
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO Student(idNum, courseId, firstName, middleName, lastName, sex) VALUES(%s,%s,%s,%s,%s,%s)", (self.idNum, self.courseId, self.firstName, self.middleName, self.lastName, self.sex))
		mysql.connection.commit()

	def update(self):
		cur = mysql.connection.cursor()
		cur.execute("UPDATE Student SET courseId=%s , firstName=%s, middleName=%s, lastName=%s , sex=%s WHERE idNum=%s", (self.courseId, self.firstName, self.middleName, self.lastName, self.sex, self.idNum))
		mysql.connection.commit()

	def delete(self):
		cur = mysql.connection.cursor()
		cur.execute("DELETE FROM Student WHERE idNum=%s", [self.idNum])
		mysql.connection.commit()

	@staticmethod
	def deleteAll():
		cur = mysql.connection.cursor()
		cur.execute('DELETE FROM Student')
		mysql.connection.commit()

class Course:

	def __init__(self, courseId, courseName):
		self.courseId = courseId
		self.courseName = courseName

	@staticmethod
	def view():
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM Course")
		dis = cur.fetchall();
		return dis

	def add(self):
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO Course(courseId, courseName) VALUES(%s,%s)", (self.courseId, self.courseName))
		mysql.connection.commit()

	def update(self):
		cur = mysql.connection.cursor()
		cur.execute("UPDATE Course SET courseId=%s , courseName=%s WHERE courseId = %s", (self.courseName, self.courseId))
		mysql.connection.commit()

	def delete(self):
		cur = mysql.connection.cursor()
		cur.execute("DELETE FROM Course WHERE courseId=%s", [self.courseId])
		mysql.connection.commit()

	@staticmethod
	def deleteAll():
		cur = mysql.connection.cursor()
		cur.execute('DELETE FROM Course')
		mysql.connection.commit()

