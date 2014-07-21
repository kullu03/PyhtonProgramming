
import sys
sys.path.append('/home/kuldsin2/PythonProgramming/PyhtonProgramming/data_structure/stack')
from stack import Stack
from binary_tree import BinaryTree

def buildParseTree(fexp):
	fplist = fexp.split()
	pStack = Stack()
	eTree = BinaryTree('')
	pStack.push(eTree)
	currentTree = eTree
	for i in fplist:
		if i == '(' :
			currentTree.setLeftChild(BinaryTree(''))
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		elif i not in ['+','-','*','/',')'] :
			currentTree.setRootVal(int(i))
			parent = pStack.pop()
			currentTree = parent
		elif i in ['+','-','*','/']:
			currentTree.setRootVal(i)
			currentTree.insertRight(BinaryTree(''))
			pStack.push(currentTree)
			currentTree = currentTree.getRightChild()
		elif i == ')':
			currentTree = pStack.pop()
		else :
			raise ValueError
	print etree

			

