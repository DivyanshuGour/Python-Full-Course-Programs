class Student:
	def __init__(self,roll=None,name=None,marks=None):
		self.roll = roll
		self.name = name
		self.marks = marks
	def input(self):
		self.roll = int(input("\nRoll : "))
		self.name = input("Name : ")
		self.marks = float(input("Marks : "))
	def show(self):
		print("\nRoll : ",self.roll)
		print("Name : ",self.name)
		print("Marks : ",self.marks)

ob1 = Student()
ob1.input()
ob1.show()




