class firstn(object):
	def __init__(self,n):
		self.n = n;
		self.nums = []
		self.num =0
	def __iter__(self):
		return self
	#def __next__(self):
	#	return self.next
	def next(self):
		if self.num < self.n:
			cur , self.num = self.num,self.num+1
			return cur
		else:
			raise StopIteration()
sum = sum(firstn(5))
print(sum)
		

		
