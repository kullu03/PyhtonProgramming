class Duck:
	def quack(self):
		print("quack quack!!!")
	def feathers(self):
		print("I have nice features!!!!")
class Person:
	def quack(self):
		print("Person imitatin the quack!!!")
	def feathers(self):
		print("I have feathures but not real one")
	def name(self):
		print ("Hey,, I am Kuldeep")
def in_the_forest(duck):
	duck.quack()
	duck.feathers()
	try:
		duck.name()
	except(AttributeError,TypeError):
		print "duck dnt have name"
def game():
	real_duck = Duck()
	kuldeep = Person()
	in_the_forest(real_duck)
	in_the_forest(kuldeep)

game()
