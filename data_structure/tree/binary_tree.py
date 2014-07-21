class BinaryTree :
	def __init__(self,rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None
	def insertLeft(self,newNode):
		if self.leftChild == None :
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t
			
	def insertRight(self,newNode):
		if self.rightChild == None :
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newnode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
			return self.rightChild

	def getLeftChild(self):
			return self.leftChild
	
	def setRootVal(self,key):
			self.key = key
	
	def getRootVal(self):
			return self.key

	def print_tree(self):
		print self.key
	
		if self.leftChild != None :
			self.leftChild.print_tree()
		if self.rightChild != None :
			 self.rightChild.print_tree() 
			

	


r = BinaryTree('a')
#print(r.getRootVal())
#print(r.getLeftChild())
r.insertLeft('b')
r.insertLeft('c')
#print(r.getLeftChild())
#print(r.getLeftChild().getRootVal())
r.insertRight('d')
r.print_tree()
#print(r.getRightChild().getRootVal())
#r.getRightChild().setRootVal('hello')
#print(r.getRightChild().getRootVal())
