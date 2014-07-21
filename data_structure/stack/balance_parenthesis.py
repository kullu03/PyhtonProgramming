from stack import Stack

def is_balanced(string):
	s = Stack()
	bal = True
	index = 0
	while index < len(string) and bal :
		if string[index] == '(' :
			s.push(string[index])
		if string[index] == ')' :
			if s.isEmpty():
				bal = False
			else:
				s.pop()
		index = index +1
	if s.isEmpty() and bal:
		print "Balanced"
	else:
		print "unbalanced"


is_balanced('(')
is_balanced('(()')
is_balanced('((()))')


	
