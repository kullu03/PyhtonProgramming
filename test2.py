import re
f=open("alice.txt","r")
text=f.readlines()
f.close()
'''for line in text:
	print line
	print'''
print "=======UNDERSTANDING REGULAR EXP========"
keyword = re.compile(r"^a.*n$")
for line in text:
	if keyword.search(line):
		print line

