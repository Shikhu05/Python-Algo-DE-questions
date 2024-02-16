# function to return the nthlargest value dictionary

d = {'a':1,'b':2, 'c':100, 'd':20, 'e':30}
n = 1

def n_large(d,n):
	v = sorted([v for v in d.values()], reverse = True)
	print(v)
	for i,c in enumerate(v):
		# print (i, c, n)
		# print(d.get(c,None))
		if i == n-1:
			return d.get(None,c)

print(n_large(d,n))
