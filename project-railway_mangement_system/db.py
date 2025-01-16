# connect db 

import mysql.connector as a 
con=a.connect(host="localhost",user="root")

# select database if exist 

c=con.cursor()
c.execute("show databases")
d1=c.fetchall()
d2=[]

for i in d1: 
	d2.append(i[0])

if 'myrailway' in d2: 
	db='use myrailway'
	c.execute(db)
else: 
	sql1="create database myrailway"
	c.execute(sql1)

	sql2="use myrailway"
	c.execute(sql2)

	sql3=""" create table train(Name varchar(50),cost integer , distance integer , date varchar(20))""" 
	c.execute(sql3)

	sql4="""create table customer(Name varchar(20),train varchar(20),payment integer ,date varchar(20),phone varchar(20))""" 
	c.execute(sql4)

	sql5="""create table bills(detail varchar(20),cost integer,date varchar(20))"""
	c.execute(sql5)

	sql6="""create table worker(Name varchar(100),work varchar(20),salary varchar(20))"""
	c.execute(sql6)
	con.commit()

print("Db created successfully....")