def mul(a,b):
	c = a * b
	if c>100:
		return c
		
a = mul(2,4)				
#if a==None:
#if id(a)==id(None):
if a is None:
	print("No Return Value !")
else:	
	print(a)



