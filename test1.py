student=["manu","manjeet","roli","roopa"]
print student
one_more =raw_input("Enter one more student")
student.append(one_more)
print student
num=input("enter an index")
if num<=len(student):
	print student[num]
else:
	print "wrong index"
student=student+["deepa","munni"]
print student
student.reverse()
print student
student.insert(1,"Mahakal")
print student
student.sort()
print student
count=0
for std in student:
	count=count+1
	if std=="roli":
		del student[count]
print student


