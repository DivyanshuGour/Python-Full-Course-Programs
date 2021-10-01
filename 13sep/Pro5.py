def fun1():
	print("Fun1 Start ... ")
	fun2()
	print("Fun1 End ... ")
def fun2():
	print("Fun2 Start ... ")
	a  = fun3()
	z = 10 * a
	print(z)
	print("Fun2 End ... ")
def fun3():
	print("Fun3 Start ... ")
	try:
		x = 34 / 0
		return x
	except Exception as ex:
		print(ex)
		raise ex
	

print("Start .... ")
fun1()
print("End .... ")




"""
				

	Raju , Gopal

			Exception ,

	1. Raju >>> 
	2. Handling ,, Raju

			3. Handling


"""















