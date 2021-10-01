# Instance Variable , Class Variable
class Student:
	def setData(self,roll,name):
			self.roll = roll
			self.name = name
	def show(self):
		print("\nRoll : ",self.roll," Name : ",self.name)

ob1 = Student()
ob2 = Student()
ob3 = Student()
#print(type(ob1))

#ob1.setData(101,'vikas')
#ob2.setData(102,'gopal')
#ob3.setData(103,'meena')

ob1.show()
ob2.show()
ob3.show()



