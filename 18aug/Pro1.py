def hello(abc):
	print("Hello : ", abc , id(abc))
	abc = 25


num = 10

print(num , id(num))

hello(num)

print(num)


