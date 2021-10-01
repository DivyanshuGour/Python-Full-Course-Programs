num = {23:'g',44:'q',11:'d',55:'p',66:'v'}

print(num)

keys = list(num.keys())

for k in keys:
	v = num.get(k)
	num.pop(k)
	num.update({v:k})	

print(num)

