print("** Voting Program **")

nat = input("Are You Indian (Y/N) : ")

if nat=='y' or nat=='Y':
	age = int(input("Your Age : "))
	if age>=18: # True block
		print("You Can Give vote !")
		print("Go Your Nearest Center !")	
	else: # False Block
		print("You Can Not Give Vote !")
		print("Try Next Time !")
else:	
	if nat=='n' or 	nat=='N':
		print("Not Allowed, Go Your Country !")
	else:
		print("Wrong Input !")		

print("** Thanks **")
