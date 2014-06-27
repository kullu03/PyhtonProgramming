def fact(n):
	if n<=1:
		return n;
	else:
		return n*fact(n-1)
value = fact(5)
print (value)
