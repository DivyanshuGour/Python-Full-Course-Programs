def add(a,b):
	c = a + b
	print("Add : ",c)
	
def mul(a,b):
	c = a * b
	print("Mul : ",c)	
	
def hello(a,b,op):
	print("Hello Students !")
	op(a,b)
	print("Good Evening !")
	
hello(34,22,add)
hello(12,4,mul)	
