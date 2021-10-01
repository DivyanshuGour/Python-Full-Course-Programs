def hello():
	print("Hello Student !")
	print("Good Evening !")
	

def test(abc):
	def xyz():
		print("Universal Indore !")
		abc() 
		print("Thanks")
	return xyz

# Decorator
ob = test(hello)	
ob()

	
 	
