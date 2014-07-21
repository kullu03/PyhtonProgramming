from stack import Stack

def infix_to_postfix_converter(exp):
	opstack = Stack()
	output = []
	prec = {}
	prec['(']=1
	prec['+']=2
	prec['-'] =2
	prec['*'] =3
	prec['/'] =3
	tokenList = exp.split()
	# n = len(exp)
	for token in tokenList :
		if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or '0123456789':
			output.append(token)
		elif token == '(' :
			opstack.push(token)
		elif token == ')' :
			while opstack.pop()!=')':
				item = opstack.pop()
				output.append(item)
		else:
			while (not opstack.isEmpty() and prec[token]<= opstack.peep()):
				output.append(opstaxk.pop())
			opstack.push(token)

	while not opstack.isEmpty():
		output.append(opstack.pop())
	return " ".join(output)

print (infix_to_postfix_converter('A*B+C*D')
print exp1
		
			
			


