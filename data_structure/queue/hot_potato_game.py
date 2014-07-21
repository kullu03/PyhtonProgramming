from queue import Queue

def hotPotato(nameList,num):
	q = Queue()
	for name in nameList :
		q.enqueue(name)
	while q.size()>1 :
		for i in range(num):
			q.enqueue(q.dequeue())

		q.dequeue()
	

	return q.dequeue()







d = hotPotato(['Kuldeep',"Manu","Manjeet","Roli","Deepa","Roopa","Akshat"],10)
print d
