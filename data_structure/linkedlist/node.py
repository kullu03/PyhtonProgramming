class Node :
	def __init__(self,data):
		self.data = data
		self.next = None
	def setdata(self,newData):
		self.data = newdata
	def getData(self):
		return self.data
	def setNext(self,newNext):
		self.next = newNext
	def getNext(self):
		return self.next


