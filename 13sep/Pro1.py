print("Start .... ")

try:
	x = int(input("X : "))
	y = int(input("Y : "))
	z = x + y
	print("Result : ",z)
except ValueError as er:
	print("\nPlease Supply Number !")

print("Thanks")
