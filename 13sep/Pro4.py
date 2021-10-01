def fun1():
	print("Fun1 Start ... ")
	fun2()
	print("Fun1 End ... ")
def fun2():
	print("Fun2 Start ... ")
	fun3()
	print("Fun2 End ... ")
def fun3():
	print("Fun3 Start ... ")
	try:
		x = 34 / 0
	except Exception as ex:
		print(ex)
	print("Fun3 End ... ")


print("Start .... ")
fun1()
print("End .... ")
