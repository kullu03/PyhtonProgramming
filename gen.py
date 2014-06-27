# generator example 

def firstn(n):
	num = 0
	while(num< n):
		yield num
		num+=1
sum_of_first_10 = sum(firstn(10))
print(sum_of_first_10)
		
	
