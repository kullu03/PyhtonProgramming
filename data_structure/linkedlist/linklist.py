from node import Node

class LinkList :
	def __init__(self,head):
		self.head = head 
		self.next  = None
	def isEmpty(self):
		return self.head == None
	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
	def size(self):
		current = self.head
		count = 0
		while current == None :
			count = count+1
			current = current.next
		return count

	def search(self,item):
		current = self.head
		found = False
		while current != None and not found :
			if current.getData() == item :
				found = True
			else:
				current = current.next
		return found
	
	def remove(self,item):
		current = self.head
		prev = False
		found = False
		while not found :
			if current.getData() == item :
				found = True
			else:
				prev = current
				current = current.next
		if prev == None :
			self.head = current.next
		else :
			previous.setNext(current.getNext())


	def printlist(self):
        	current = self.head
                while current == None :
			print current.getData()
                        current = current.next

