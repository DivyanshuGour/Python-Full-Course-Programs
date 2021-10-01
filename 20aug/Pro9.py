def hello(ob):
	print(ob , id(ob))
	ob.append(100)

num = [4,5,3,2,6,7,4,6]

print(num , id(num))

hello(num.copy())

print(num)


