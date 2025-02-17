import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",db="myrailway")
# Systen passwork login 

def sigin(): 
	print("\n")
	print("--------------->>>>>>>>>>>>>>welcome,Railway Management System<<<<<<<<<<<<<<<<<<<<<<<<<<---------------")
	print("\n")
	p=input("enter the password")
	if p=="rms111":
		options()
	else: 
		sigin()


# Project working options 

def options(): 
	print(""" 
			1. Add Train 
			2. Book Train 
			3. Add Bill 
			4. Add Worker 
			5. Display Train 
			6. Display Payments 
			7. Display Bills 
			8. Display Workers 

		""")
	choice=input("enter the options :")
	while True:
		if choice=="1": 
			AddTrain()
			break
		elif choice=="2": 
			BookTrain()
			break
		elif choice=="3": 
			AddBill()
			break
		elif choice=="4": 
			AddWorker()
			break
		elif choice=="5": 
			DisplayTrain()
			break
		elif choice=="6": 
			DisplayPayments()
			break
		elif choice=="7":
			DisplayBills()
			break
		elif choice=="8": 
			DisplayWorker()
			break

		else:
			
			print("enter the correct options.....")
			options()


# function to add new Trains data into Train table 

def AddTrain():
	n=input("Train Name : ")
	c=input("Cost : ")
	b=input("Distance : ")
	d=input("Date : ")
	data=(n,c,b,d)
	sql="insert into train values(%s,%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inserted successfully....")
	options()


def BookTrain(): 
	n=input("customer name : ")
	s=input("Train")
	py=int(input("Payment : "))
	d=input("Date : ")
	p=input("Phone : ")
	data=(n,s,py,d,p)

	sql="insert into customer values(%s,%s,%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inserted successfully.....")
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
	print("Data inserted successfully")
	options()


def AddWorker():
	n=input("Name : ")
	w=input("work : ")
	s=input("Salary :")
	data=(n,w,s) 
	sql="insert into woker values(%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inserted successfully......")
	options()


def DisplayTrain():
	sql="select*from Train"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()

	for i in d: 
		
			print("Name : ",i[0])
			print("cost :",i[1])
			print("Distance :",i[2])
			print("Date : ",i[3])
			
			print("-----------------------------------")
	options()

def DisplayPayments(): 
	sd=input("Date : ")
	sql="select*from customer"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()

	for i in d: 
		if i[3]==sd:
			print("Name : ",i[0])
			print("Train :",i[1])
			print("Payment :",i[2])
			print("Date : ",i[3])
			print("Phone : ",i[4])
			print("-----------------------------------")
	options()

def DisplayBills():
	sql=input("Date : ")
	sql="select*from bills"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d:
		print("Detail : ",i[0])
		print("Cost : ",i[1])
		print("Date : ",i[2])
		print("----------------------------------------")
	options()


def DisplayWorker(): 
	sql="select*from woker"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d: 
		print("Name :",i[0])
		print("Work : ",i[1])
		print("Salary : ",i[2])
		print("------------------------------------------------")

	options()
sigin()

