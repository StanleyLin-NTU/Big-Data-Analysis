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


F1=open("foxup.txt",'r',encoding="UTF-8")
F2=open("foxdown.txt",'r',encoding="UTF-8")
F3=open("foxconn.txt",'r',encoding="UTF-8")
F10=open("typ_fox.txt",'r',encoding="UTF-8")

F7=open("result_fox","w",encoding="UTF-8")
F8=open("nonodata_typ_fox","w",encoding="UTF-8")
F9=open("nonodata_fox","w",encoding="UTF-8")
#IND=open("indcies.txt",'r',encoding="UTF-8")
#Output=open("df_台積電_6.txt",'w')
typ=[]
a1=F1.read().splitlines()
a2=F2.read().splitlines()
typ=F10.read().splitlines()

a=a1+a2
#print(a)
#print(typ)
b=F3.read().splitlines()
t_b=[]
t_typ=[]

for i in range(0,len(b)):
	if(typ[i]!="nodata"):
		t_b.append(b[i])
		t_typ.append(typ[i])
		F8.write(typ[i])
		F8.write("\n")

b=t_b
typ=t_typ
for i in range(0,len(b)):
	F9.write(b[i])
	F9.write("\n")

print(len(b))
print(len(typ))
#print(len(b))
#ind=IND.read().splitlines()
vector=[]
for s in range(0,len(b)):
	vector.append([])
#print(vector)

for i in range(0,len(b)):
	for j in range(0,len(a)):
		if(a[j] in b[i]):
			#print (a[i])
			vector[i].append(b[i].count(a[j]))
		else:
			vector[i].append(0)



#上面已經找到新聞數量條數的0 1向量了（長度各為245)
#以下為待辦事項
#睡覺囉
#設定target的vector
#F4=open("nonodata_target",'r',encoding="UTF-8")
#target=F4.read().splitlines()
target=b
print(len(target))
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
target_nor=t_Vector
#vector_nor=Normalize(vector)
#print(vector_nor[0])
#print(vector_nor[1])
#target_nor= Normalize(t_Vector)
#print(vector_nor[0])
#print(target_nor[0])
#對比filter掉1
result_arr=[]
vec_result=[0]*len(vector_nor)
for k in range(0,len(target_nor)):
	target_numpy=np.array(target_nor[k])
	#print(target_numpy)
	for l in range(0,len(vector_nor)):
		try_numpy=np.array(vector_nor[l])
		vec_result[l]=np.linalg.norm(try_numpy-target_numpy)
	arr=np.array(vec_result)
	index=arr.argsort()[:3]
	index_pre=arr.argsort()[4]
	up=0
	down=0
	common=0
	for i in range(0,len(index)):
		#print(typ[index[i]])
		if(typ[index[i]]=="goup"):
			up=up+1
		if(typ[index[i]]=="godown"):
			down=down+1
		if(typ[index[i]]=="common"):
			common=common+1
	if(up>=2):
		F7.write("goup\n")
		result_arr.append("goup")
	if(down>=2):
		F7.write("godown\n")
		result_arr.append("godown")
	if(common>=2):
		F7.write("common\n")
		result_arr.append("common")
	if(up==1 and down==1 and common==1):
		F7.write(typ[index_pre])
		F7.write("\n")
		result_arr.append(typ[index_pre])
	#print(len(index))
acc=0
for i in range(0,len(result_arr)):
	if(result_arr[i]==typ[i]):
		acc=acc+1

print(acc/len(result_arr))
	#txtname1="Result"+str(k)+".txt"
	#txtname2="value"+str(k)+".txt"
	#txtname3="index"+str(k)+".txt"
	#F4=open(txtname1,'w',encoding="UTF-8")
	#F5=open(txtname2,'w',encoding="UTF-8")
	#F6=open(txtname3,'w',encoding="UTF-8")
	#print(b[index.item(0)])
	#for z in range(1,len(index)):
	#	F4.write(b[index.item(z)])
	#	F5.write(str(vec_result[index.item(z)]))
		#F6.write(str(ind[index.item(z)]))
	#	F4.write("\n")
	#	F5.write("\n")
		#F6.write("\n")






#排序前六名輸出新聞


