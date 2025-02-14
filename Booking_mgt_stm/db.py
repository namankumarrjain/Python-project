# connect database 
import mysql.connector as a 
con=a.connect(host="localhost",user="root")

#select database if exist 

c=con.cursor()
c.execute("show databases")
d1=c.fetchall()
d12=[]

for i in d1: 
	d12.append(i[0])

if 'bshop' in d12: 
	sql="use bshop"
	c.execute(sql)
else: 
	sql1="create database bshop"
	c.execute(sql1)

	sql2="use bshop"
	c.execute(sql2)

	sql3="""create table book(Name varchar(50), Author varchar(50),costprice integer,sellprice integer,Date varchar(20))"""
	c.execute(sql3)

	sql4="""create table customer(Name varchar(20),Book varchar(25),payment varchar(8),Date varchar(20),phone varchar(20))"""
	c.execute(sql4)

	sql5="""create table bills(detail varchar(20),cost integer , date varchar(20))""" 
	c.execute(sql5)

	sql6="""create table worker(Name varchar(100),work varchar(20),salary varchar(20))"""
	c.execute(sql6)

	con.commit()



