def test(abc):
	def xyz():
		print("Universal Indore !")
		abc() 
		print("Thanks")
	return xyz

@test
def hello():
	print("Hello Student !")
	print("Good Evening !")
	
hello()

	
 	
