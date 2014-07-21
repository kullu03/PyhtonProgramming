from stack import Stack
import re

def eval_postfix(expr):
	s = Stack()
	s.push(12)
	#exp_list = exp.split()
	exp ='123+456*/'
	exp_list = re.split("([^0-9])", expr)
	print exp_list
	for e in exp_list :
		if e == ' ' or e == '':
			print e
		elif e == '+':
			a = s.pop()
			b = s.pop()
			c = b + a
			s.push(c)
		elif e == '*':
			a = s.pop()
                        b = s.pop()
                        c = b * a
                        s.push(c)
		elif e == '/':
			a = s.pop()
                        b = s.pop()
                        c = b/a
                        s.push(c)
		elif e == '-':
			a = s.pop()
                        b = s.pop()
                        c = b - a
                        s.push(c)
		else:
			s.push(int(e))
	return s.pop()

result = eval_postfix('123+456*/')

print result
