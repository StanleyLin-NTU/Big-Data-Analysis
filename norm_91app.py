import csv
f1=open("/Users/StanleyLIn/Desktop/Group1","r")
Pay=open("Pay_type_norm1",'w')
SRC=open("SRC_type_norm1",'w')
for row in csv.DictReader(f1):
	if(row["PayType"]=="到店取貨付款"):
		Pay.write("1")
		Pay.write("\n")
	if(row["PayType"]=="信用卡一次"):
		Pay.write("2")
		Pay.write("\n")
	if(row["Source"]=="AndroidAPP"):
		SRC.write("1")
		SRc.write("\n")
	if(row["Source"]=="iOSAPP"):
		SRC.write("2")
		SRC.write("\n")
	if(row["Source"]=="WEB"):
		SRC.write("3")
		SRC.write("\n")