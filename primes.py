def is_prime(number):
	if number in(0,1):
		return False;
	for element in range(2,number):
		if number % element == 0:
			return False
	return True
def next_prime(number):
	index = number
	while True:
		index = index+1
		if(is_prime(index)):
			print(index)
			return
is_prime(7)
next_prime(100)
