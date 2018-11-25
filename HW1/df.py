F1=open("result_台積電_6.txt",'r',encoding="UTF-8")
F2=open("台積電.txt",'r',encoding="UTF-8")
Output=open("df_台積電_6.txt",'w')
a=F1.read().splitlines()
print(a)
b=F2.readlines()
#print(b)
c=[0]*len(a)

for i in range(0,len(a)):
	for j in range(0,len(b)):
		if(a[i] in b[j]):
			print (a[i])
			c[i]+=1

for k in range(0,len(c)):
	Output.write(str(c[k]))
	Output.write("\n")

