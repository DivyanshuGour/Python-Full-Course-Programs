print("Start .... ")

try:
	x = int(input("X : "))
	y = int(input("Y : "))

	data = {'a':x,'b':y}
	z = data['a'] / data['c']
	print("Result : ",z)
except ValueError as er:
	print("\nPlease Supply Number  ! ")
except ZeroDivisionError as er:
	print("\nZero Not Allowed !")
except Exception as ex:
	print("Error  : ")

print("Thanks")
