# demonstration of private method private function and private attribute #


class withPrivate:
	@classmethod
	def sayHello(self):
		print "Hello Boss,I am public method"
	@classmethod
	def __secretHello(self):
		print "I am not easily accesible outside the class"



object =  withPrivate()
#object.sayHello()
_withPrivate__secretHello()

	
