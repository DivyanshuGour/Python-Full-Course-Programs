# default argument
def add(a , b , c=5 , d=1):
	print(a,b,c,d)
	z = a + b + c + d
	print("Z : ",z)

# named / keyword argument
add(6,5,d=9) # a=6,b=5,d=9
add(d=3,a=4,c=1,b=7)

add(7,4,d=3,c=1)





