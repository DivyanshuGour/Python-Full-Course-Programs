num = [44,(55,[66,44],33),22,[11,(88,77),(66,55),44],33]

print(len(num))
print(num[3][1][0])
num[3][1] = 55
print(num)
#num[3][2][1] = 22
#print(num)

num[1][1].append(11)
print(num)

#num[1][0] = 11




