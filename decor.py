def is_even(num):
	''' returns True if num is even '''
	return (num%2==0)
def count_occurences(target_list,predicate):
	'''return the count of oocurences in list for which predicate is True '''
	count =sum([1 for i in target_list if predicate(i)])
	print (count)
target_list = [2,4,6,7,8,9]
predicate = is_even
count_occurences(target_list,is_even)
