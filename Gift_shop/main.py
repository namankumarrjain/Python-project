import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",db="gshop")

# System password Login 

def sigin(): 
	print("\n")
	print("------------>>>>>>>>welcome,Gift Shop [GS] <<<<<<<<<<<<<<------------")
	print("\n")
	p=input("System password :")
	if p=="dgs111": 
		options()
	else: 
		sigin()


# project working options 

def options(): 
	print(""" 
					1. Add Gift
					2. Sell Gift
					3. Add Bill
					4. Add worker 
					5. Display Gifts 
					6. Display Payments 
					7. Display Bills 
					8. Display workers 
		""")
	choice=input("enter the choice : ")
	while True:
		if (choice=='1'): 
			AddGift()
		elif (choice=='2'): 
			SellGift()
		elif (choice=='3'): 
			AddBill()
		elif (choice=='4'):
			AddWorker()
		elif (choice=='5'): 
			DisplayGift()
		elif (choice=='6'): 
			DisplayPayments()
		elif (choice=='7'):
			DisplayBills()
		elif (choice=='8'): 
			DisplayWorkers()
		else: 
			print("enter the choice again.....")
			options()


# AddGift

def AddGift(): 
	n=input("Name : ")
	c=input("Cost : ")
	b=input("Buy : ")
	d=input("Date : ")
	data=(n,c,b,d)
	sql="insert into Gifts values(%s,%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inseted successfully.....")
	options()

def SellGift(): 
	n=input("Name : ")
	g=input("Gift : ")
	py=int(input("Payment : "))
	d=input("Date : ")
	p=input("Phone : ")
	data=(n,g,py,d,p)

	sql="insert into customer values(%s,%s,%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inseted successfully.....")
	options()

def AddBill(): 
	dt=input("Detail : ")
	c=input("Cost : ")
	d=input("Date : ")
	data=(dt,c,d)

	sql="insert into bills values(%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inseted successfully.....")
	options()

def AddWorker(): 
	n=input("Name : ")
	w=input("Work : ")
	s=input("salary : ")
	
	data=(n,w,s)

	sql="insert into worker values(%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inseted successfully.....")
	options()

def DisplayGift(): 
	
	sql="select*from gifts"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d: 
			print("Name :",i[0],"cost:",i[1],"Buy :",i[2],"Date : ",i[3])
			print("-------------------------------------------------------")
	options()

def DisplayPayments(): 
	sd=input("Date : ")
	sql="select*from customer"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d: 
		if i[3]==sd: 
			print("Name :",i[0],"Gift:",i[1],"Payment :",i[2],"Date : ",i[3],"phone : ",i[4])
			print("-------------------------------------------------------")
	options()
def DisplayBills(): 
	
	sql="select*from bills"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d:  
		print("Detail :",i[0],"cost:",i[1],"Date : ",i[2])
		print("-------------------------------------------------------")
	options()
def DisplayWorkers():
	sql="select*from worker"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d: 
		print("Name :",i[0],"work:",i[1],"salary :",i[2])
		print("-------------------------------------------------------")
	options() 
sigin()

