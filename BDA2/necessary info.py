F1=open("words.txt",'r',encoding="UTF-8")
F2=open("foxconn.txt",'r',encoding="UTF-8")
Output_AND=open("output_AND.txt",'w')
Output_OR=open("output_OR.txt",'w')
a=F1.read().splitlines()
print(a)
b=F2.read().splitlines()
#print(b)
AND=[0]*len(a)
OR=[0]*len(a)
for i in range(0,len(a)):
	for j in range(0,len(b)):
		if(a[i] in b[j] and "鴻海" in b[j]):
			AND[i]=AND[i]+1
		if(a[i] in b[j] or "鴻海" in b[j]):
			OR[i]=OR[i]+1

for k in range(0,len(a)):
	Output_AND.write(str(AND[k]))
	Output_OR.write(str(OR[k]))
	Output_AND.write("\n")
	Output_OR.write("\n")

