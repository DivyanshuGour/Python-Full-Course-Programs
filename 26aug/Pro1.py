num =[1,2,3,4,[5,6,7,[8,[9,10],11,[12,[13,[45],14],15],16,17]],18,19,20]

def listprint(x):
	for a in x:
		if type(a) is list:
			listprint(a)
		else:
			print(a)


for x in num:
	if type(x) is list:
		listprint(x)
	else:
		print(x) 
