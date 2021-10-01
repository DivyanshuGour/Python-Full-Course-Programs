def add(a,b):
	c = a + b
	print("Add : ",c)
	
def mul(a,b):
	c = a * b
	print("Mul : ",c)	
	
def hello(a,b,op):
	print("Hello Students !")
	if op==1:
		add(a,b)
	elif op==2:
		mul(a,b)		
	print("Good Evening !")
	
hello(34,22,1) # add:1 mul:2
hello(12,4,2)	
