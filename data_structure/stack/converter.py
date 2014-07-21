from stack import Stack
def decimal_to_anybase(n,base):
	s= Stack()
	digits = '0123456789ABCDEF'
	res = ""
	while n > 0 :
		s.push(n%base)
		n = n/base
	while (not s.isEmpty()):
		res =res + str(digits[(s.pop())])
	return res

bins = decimal_to_anybase(42,8)
print bins


	
