
import mysql.connector as a 
con=a.connect(host="localhost",user="root",db="myrailway")

# AddTrain
def AddTrain(): 
	n=input("Train Name : ")
	c=input("Cost :")
	b=input("Distance : ")
	d=input("Date : ")
	data=(n,c,b,d)
	sql="insert into train values(%s,%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inserted successfully.....")
	options()

#BookTrain
def BookTrain(): 
	n=input("Customer Name : ")
	s=input("Train :")
	py=int(input("Payments : "))
	d=input("Date : ")
	p=input("Phone : ")

	data=(n,s,py,d,p)
	sql="insert into customer values(%s,%s,%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inserted successfully.....")
	options()

#AddBills
def AddBill(): 
	dt=input("Detail : ")
	c=input("Cost : ")
	d=input("Date : ")
	data=(dt,c,d)
	sql="insert into bills values(%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()
	print("Data inserted successfully.....")
	options()


#AddWorker
def AddWorker(): 
	n=input("Name : ")
	w=input("Work : ")
	s=input("Salary : ")
	data=(n,w,s)
	sql="insert into worker values(%s,%s,%s)"
	c=con.cursor()
	c.execute(sql,data)
	con.commit()

	print("Data inserted successfully.....")
	options()


#DisplayTrain

def DisplayTrain(): 
	sql="select*from train"
	
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	
	for i in d: 
		print("Name :",i[0])
		print("Cost : ",i[1])
		print("Distance : ",i[2])
		print("Date : ",i[3])
		print("---------------------------------")
	options()

#DisplayPayments 
def DisplayPayments(): 
	sd=input("Date : ")
	sql="select*from customer"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()

	for i in d: 
		if i[3]==sd: 
			print("Name :",i[0])
			print("Cost : ",i[1])
			print("Distance : ",i[2])
			print("Date : ",i[3])
			print("Phone : ",i[4])
			print("---------------------------------")
	options()

#DisplayBills
def DisplayBills(): 
	sql="select*from bills"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()

	for i in d: 
		print("Detail : ",i[0])
		print("Cost : ",i[1])
		print("Date : ",i[2])
		print("------------------------------------")
	options()


#DisplayWorker
def DisplayWorkers(): 
	sql="select*from worker"
	c=con.cursor()
	c.execute(sql)
	d=c.fetchall()
	for i in d: 
		print("Name : ",i[0])
		print("Work : ",i[1])
		print("Salary :",i[2])
		print("----------------------------------------")
	options()


# Working options 
def options(): 
	print(""" 

		1. Add Train 
		2. Book Train 
		3. Add Bill 
		4. Add worker 
		5. Display train 
		6. Display payments 
		7. Display Bills 
		8. Display workers 

		""")

	choice=input("select options : ")
	while True: 
		if(choice=="1"):
			AddTrain()
		elif(choice=="2"): 
			BookTrain()
		elif(choice=="3"): 
			AddBill()
		elif(choice=="4"): 
			AddWorker()
		elif(choice=="5"): 
			DisplayTrain()
		elif(choice=="6"): 
			DisplayPayments()
		elif(choice=="7"): 
			DisplayBills()
		elif(choice=="8"): 
			DisplayWorkers()
		else: 
			print("Thank! you")
options()