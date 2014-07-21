from stack import Stack
def decimal_to_binary(n):
	s= Stack()
	bins = ""
	while n > 0 :
		s.push(n%2)
		n = n/2
	while (not s.isEmpty()):
		bins =bins + str(s.pop())
	return bins

bins = decimal_to_binary(42)
print bins


	
