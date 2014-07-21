from deque import Deque

def isPalindrome(string):
	d = Deque()
	for c in string :
		d.addRear(c)
	while(d.size()>1):
		a = d.removeFront()
		b = d.removeRear()
		if a != b:
			return False
	return True


print(isPalindrome("lsdkjfskf"))
print(isPalindrome("radar"))
