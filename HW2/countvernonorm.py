from math import sqrt,pow
import numpy as np

def Normalize (ListofList):
	x=[]
	for s in range(0,len(ListofList)):
		x.append([])
	for i in range(0,len(ListofList)):
		length=0
		for j in range(0,len(ListofList[i])):
			length=length+pow(((ListofList[i])[j]),2)
		r= sqrt(length)
		#print(r)
		length2=0
		for j in range(0,len(ListofList[i])):
			x[i].append((ListofList[i])[j]/r)
	return x


F1=open("words.txt",'r',encoding="UTF-8")
F2=open("foxconn.txt",'r',encoding="UTF-8")
F3=open("target_new.txt",'r',encoding="UTF-8")
IND=open("indcies.txt",'r',encoding="UTF-8")
#Output=open("df_台積電_6.txt",'w')
a=F1.read().splitlines()
#print(a)
b=F2.read().splitlines()
#print(len(b))
ind=IND.read().splitlines()
vector=[]
for s in range(0,len(b)):
	vector.append([])
#print(vector)





#上面已經找到新聞數量條數的0 1向量了（長度各為245)
#以下為待辦事項
#睡覺囉
#設定target的vector
target=F3.read().splitlines()
#print(target)
#print(len(target))
t_Vector=[]
for s in range(0,len(target)):
	t_Vector.append([])

for i in range(0,len(target)):
	for j in range(0,len(a)):
		if(a[j] in target[i]):
			#print (a[i])
			t_Vector[i].append(target[i].count(a[j]))
		else:
			t_Vector[i].append(0)
#標準化（單位向量）
vector_nor=vector
#print(vector[0])
#print(vector_nor[0])
#print(vector_nor[1])
target_nor= t_Vector
#print(vector_nor[0])
#print(target_nor[0])
#對比filter掉1
vec_result=[0]*len(vector_nor)
for k in range(0,len(target_nor)):
	target_numpy=np.array(target_nor[k])
	#print(target_numpy)
	for l in range(0,len(vector_nor)):
		try_numpy=np.array(vector_nor[l])
		vec_result[l]=sum(target_numpy*try_numpy)
	arr=np.array(vec_result)
	index=arr.argsort()[-7:][::-1]
	#print(len(index))
	txtname1="Result"+str(k)+".txt"
	txtname2="value"+str(k)+".txt"
	txtname3="index"+str(k)+".txt"
	F4=open(txtname1,'w',encoding="UTF-8")
	F5=open(txtname2,'w',encoding="UTF-8")
	F6=open(txtname3,'w',encoding="UTF-8")
	#print(b[index.item(0)])
	for z in range(1,len(index)):
		F4.write(b[index.item(z)])
		F5.write(str(vec_result[index.item(z)]))
		F6.write(str(ind[index.item(z)]))
		F4.write("\n")
		F5.write("\n")
		F6.write("\n")



#排序前六名輸出新聞


