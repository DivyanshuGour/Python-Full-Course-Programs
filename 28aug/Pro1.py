class Student:
	def __init__(self,roll=None,name=None,marks=None):
		self.roll = roll
		self.name = name
		self.marks = marks
	def show(self):
		print("\nRoll : ",self.roll)
		print("Name : ",self.name)
		print("Marks : ",self.marks)

ob1 = Student(101,'vikas',234.45)
ob2 = Student(102,'meena',254.22)
ob3 = Student()

ob1.show()
ob2.show()
ob3.show()


