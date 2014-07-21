from stack import Stack

def rev_string(string):
	s = Stack()
	rev_s = ' '
	for char in string :
		s.push(char)
	while  not s.isEmpty():
		rev_s = rev_s + s.pop()
	return rev_s
