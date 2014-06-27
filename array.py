def bs(l,n):
	b= l[0]
	e = l[-1]
	while(b<=e):
		mid = (b+e)/2
		if(l[mid] == n):
			return mid
		elif(l[mid]<n):
			b=mid+1;
		else:
			e = mid-1
	print "element does not exist"	
num= [1,2,3,4,5,9,8,9]
n = 6
item = bs(num,9)
print(item)
