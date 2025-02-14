import mysql.connector 
con=mysql.connector.connect(host="localhost",user="root",db="bshop")


# System password login 

def signin(): 
	print("\n")
	print("------------>>>>>>>welcome,Agarwal Book Shop Delhi<<<<<<<<<-----------")
	print("\n")
	p=input("System password")
	if p=="abs111": 
		options()
	else: 
		signin()


# Project working Options 

def options(): 
	print(""" 
				Agarwal Book Shop 
		--------------------------------------------
			1. Add Book			5. Display Books 
			2. Sell Book 		6. Display payments 
			3. Add Bill 		7. Display Bills
			4. Add worker 		8. Display workers 

		""")
	choice=input("Select options : ")
	while True: 
		if(choice=="1"):
			AddBook()
		elif(choice=="2"): 
			SellBook()
		elif(choice=="3"): 
			AddBill()
		elif(choice=="4"): 
			AddWorker()
		elif(choice=="5"): 
			DisplayBook()
		elif(choice=="6"): 
			DisplayPayments()
		elif(choice=="7"): 
			DisplayBills()
		elif(choice=="8"): 
			DisplayWorkers()
			
		else: 
			print("Enter Again......")
			options()


def AddBook(): 
	n=input("Name : ")
	a=input("Author : ")
	c=input("Cost price : ")
	s=input("Selling price : ")
	d=input("Date : ")
	data=(n,a,c,s,d)
	sql="insert into book values(%s,%s,%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inseted successsfully.....")
	options()

def SellBook(): 
	n=input("Name : ")
	s=input("Book : ")
	py=input("Payment : ")
	d=input("Date : ")
	p=input("Phone : ")
	data=(n,s,py,d,p)
	sql="insert into book values(%s,%s,%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inseted successsfully.....")
	options()


def AddBill():
	dt=input("Details : ")
	c=input("Cost : ")
	d=input("Date : ")
	data=(dt,c,d)
	sql="insert into bills values(%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inseted successsfully")
	options()

def AddWorker():
	n=input("Name : ")
	w=input("Work : ")
	s=input("Salary : ")
	data=(n,w,s)
	sql="insert into worker values(%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inserted successsfully")
	options()


def DisplayBook(): 
	sd=input("Date : ")
	sql="select*from Book"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d: 
		if i[4]==sd: 
			print("Name : ",i[0],"Author : ",i[1],"Cost :",i[2],"Buy : ",i[3],"Date : ",i[4])
			print("---------------------------------------------")
	options()

def DisplayPayments():
	sd=input("Date : ")
	sql="select*from Book"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d: 
		if i[3]==sd: 
			print("Name : ",i[0],"Book : ",i[1],"Payment :",i[2],"Date : ",i[3],"Phone : ",i[4])
			print("---------------------------------------------")
	options()

def DisplayBills(): 
	sd=input("Date : ")
	sql="select*from Book"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d: 
			print("Details : ",i[0],"Cost :",i[1],"Date : ",i[2])
			print("---------------------------------------------")
	options()

def DisplayWorkers(): 
	sql='select*from worker'
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d: 
		print("Name : ",i[0],"work : ",i[1],"salary : ",i[2])
		print("--------------------------------------------")
	options()
signin()
