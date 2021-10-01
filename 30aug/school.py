class Result:
	def process(self,marks):
		total = sum(marks)
		per = total/5
		print("Total Marks : " , total)
		print("Percentage : " , per)

class Exam:
	# class variable
	subjects = ["Hindi","English","Physics","Chemistry","Maths"]
	def __init__(self):
		self.title = None
		self.marks = dict()
	def inputExam(self):
		self.title = input("\nExam Title : ")
		for sub in Exam.subjects:
			num = float(input(sub + " >> "))
			self.marks[sub] = num
	def showExam(self):
		res = Result()
		print("\nExam Title  : " , self.title)
		for sub in Exam.subjects:
			print("\t",sub , " : " , self.marks.get(sub))
		res.process(self.marks.values())
class Student:
	def __init__(self):
		self.roll = None
		self.name = None
		self.exams = list()
	def input(self):
		self.roll = input("Roll : ")
		self.name = input("Name : ")
	def addExam(self):
		ob =  Exam()
		ob.inputExam()
		self.exams.append(ob)
	def show(self):
		print("\nRoll Number : " , self.roll," Name : ",self.name)
		print("Exam Given : ",len(self.exams))
		for ex in self.exams:
			ex.showExam()

ob = Exam()
ob.inputExam()
ob.showExam();



""" 
	Relationship between Objects  :		
			1. Use - A
			2. Has - A 
			3. Is - A ( Inheritance )
"""









