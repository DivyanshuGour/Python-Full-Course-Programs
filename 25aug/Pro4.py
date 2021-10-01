num = [
	23,[34,5,45],12,23,[34,45,7,78],[89,54,4],34
]

for x in num:
	if type(x) is list:
		for a in x:
			print(a)
	else:
		print(x)



