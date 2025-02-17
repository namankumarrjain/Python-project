import mysql.connector 

con=mysql.connector.connect(host="localhost",user="root")


# select database
c=con.cursor()
c.execute("show databases")
d1=c.fetchall()
d2=[]
for i in d1: 
	d2.append(i[0])
if "myrailway" in d2: 
	sql="use myrailway"
	c.execute(sql)
else: 
	sql1="create database myrailway"
	c.execute(sql1)

	sql2="use myrailway"
	c.execute(sql2)

	sql3="""create table train(Name varchar(50),cost integer , distance integer , date varchar(20))"""
	c.execute(sql3)

	sql4="""create table customer(Name varchar(20),Train varchar(25),payment integer ,Date varchar(20),Phone varchar(20))"""
	c.execute(sql4)

	sql5="""create table bills(Detail varchar(20),cost integer , date varchar(20))"""
	c.execute(sql5)

	sql6="""create table woker(Name varchar(100),work varchar(20),salary varchar(20))"""
	c.execute(sql6)
	con.commit()
